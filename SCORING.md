# Scoring Algorithm Design

## Overview

The scorer does a single left-to-right pass over tokens and returns an integer score:

- **Positive score** → `POSITIVE`
- **Negative score** → `NEGATIVE`
- **Zero** → `NEUTRAL`

## Data model

All word scores live in a single `WORD_WEIGHTS` dict in `dataset.py`. The sign of the value indicates sentiment direction; the magnitude indicates strength:

| Weight | Meaning         | Examples                        |
|--------|-----------------|---------------------------------|
| +2     | Strong positive | love, amazing, awesome          |
| +1     | Positive        | happy, great, good, excited, !  |
| 0      | Neutral         | (any word not in the dict)      |
| -1     | Negative        | sad, bad, tired, stressed       |
| -2     | Strong negative | hate, terrible, awful           |

Two additional sets in `dataset.py` modify how scores are applied:

- **`NEGATION_WORDS`** — flip the sign of the next sentiment word (`not`, `never`, `no`, `dont`, …)
- **`AMPLIFIER_WORDS`** — double the magnitude of the next sentiment word (`very`, `so`, `too`, `really`, …)

## Flag mechanics

The scorer uses two boolean flags: `negate_next` and `amplify_next`.

### Modifier tokens skip the flag reset

When a negation or amplifier word is encountered, the flag is set and the loop moves to the next token via `continue`. This skips the flag-reset at the bottom of the loop, so flags accumulate across consecutive modifiers.

```
"not very happy"
  → "not"   sets negate_next=True,  continue  (reset skipped)
  → "very"  sets amplify_next=True, continue  (reset skipped)
  → "happy" gets: +1 × 2 (amplify) × -1 (negate) = -2
  → both flags reset
```

### Flags reset on all non-modifier tokens

Both flags reset whenever a non-modifier token is reached — even if that token has no sentiment score. This prevents negation from leaking across multiple unrelated words.

```
"not something happy"
  → "not"       sets negate_next=True, continue
  → "something" has no sentiment; flags reset to False
  → "happy"     scores normally: +1
```

Compare with:

```
"not happy"
  → "not"   sets negate_next=True, continue
  → "happy" gets +1 × -1 = -1
```

The negation window is one word only, unless amplifiers appear between the negation and the target (in which case the amplifier also continues without resetting).

## Emoji handling

Emojis are handled via an alias map (`EMOJI_MAP` in `dataset.py`) rather than adding them directly to `WORD_WEIGHTS`. During preprocessing, each emoji character is replaced with its word alias (e.g., `😭` → `"hate"`, `😊` → `"happy"`).

This design has two benefits:

1. **Reuses existing weights** — `😊` gets the same score as `"happy"` (+1) without duplication.
2. **Responds to modifiers** — `"not 😊"` becomes `"not happy"`, so negation flips the score to -1. If emojis were scored in a separate pass, the negation flag would never reach them because the emoji would already be consumed before negation could apply.

A single token can contain multiple emojis (e.g., `"🥰🥰🥰"`). The preprocessor scans character by character, replacing each emoji independently, so that token produces three `"love"` aliases → score +6.

## Why MIXED is hard

A single integer score collapses opposing sentiments into a net value, losing the information needed to detect mixed feelings. A sentence like *"Feeling tired but kind of hopeful"* has one negative word (`tired`) and no positive words in `WORD_WEIGHTS`, so it scores -1 → `NEGATIVE`, not `MIXED`.

Possible approaches to detect mixed sentiment in the future:

- **Clause splitting** — split on conjunctions like "but", "yet", "although" and score each clause separately. If the signs differ, return `MIXED`.
- **Dual tracking** — track positive and negative totals separately. If both are nonzero, return `MIXED`; otherwise resolve by comparing magnitudes.

Both approaches require changes beyond the single integer score that `score_text` currently returns.
