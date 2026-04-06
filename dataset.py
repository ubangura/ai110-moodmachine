"""
Shared data for the Mood Machine.

This file defines:
  - MoodLabel: enum of allowed mood labels
  - WORD_WEIGHTS: mapping of sentiment words (and punctuation) to integer scores
  - EMOJI_MAP: mapping of emoji characters to word aliases in WORD_WEIGHTS
  - NEGATION_WORDS: words that flip the sign of the next sentiment token
  - AMPLIFIER_WORDS: words that double the magnitude of the next sentiment token
  - LABELED_POSTS: list of (post, MoodLabel) tuples for evaluation and training
"""

from enum import Enum
from typing import Dict


class MoodLabel(str, Enum):
    """Allowed mood labels for the Mood Machine."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    MIXED = "mixed"


# ---------------------------------------------------------------------
# Sentiment word weights
# ---------------------------------------------------------------------

WORD_WEIGHTS: Dict[str, int] = {
    # Positive
    "happy": 1,
    "great": 1,
    "good": 1,
    "excited": 1,
    "fun": 1,
    "chill": 1,
    "relaxed": 1,
    # Strong positive
    "love": 2,
    "amazing": 2,
    "awesome": 2,
    # Negative
    "sad": -1,
    "bad": -1,
    "angry": -1,
    "upset": -1,
    "tired": -1,
    "stressed": -1,
    "boring": -1,
    # Strong negative
    "hate": -2,
    "terrible": -2,
    "awful": -2,
    # Punctuation
    "!": 1,
}

EMOJI_MAP: Dict[str, str] = {
    # Positive
    "😊": "happy",
    "😄": "happy",
    "😁": "happy",
    "🙂": "good",
    "😂": "fun",
    "🤣": "fun",
    "🥰": "love",
    "😍": "love",
    "❤️": "love",
    "🔥": "awesome",
    "💪": "great",
    "🎉": "excited",
    "✨": "great",
    # Negative
    "😢": "sad",
    "😞": "sad",
    "😔": "sad",
    "🥲": "sad",
    "😭": "hate",
    "😡": "angry",
    "🤬": "hate",
    "😤": "angry",
    "💀": "terrible",
    "😒": "boring",
    "🙄": "boring",
    "😩": "stressed",
    "😫": "tired",
}

# Punctuation-stripped forms (e.g. "dont" not "don't").
NEGATION_WORDS = {
    "not",
    "never",
    "no",
    "dont",
    "doesnt",
    "isnt",
    "wasnt",
    "arent",
    "cant",
    "wont",
}

AMPLIFIER_WORDS = {
    "very",
    "so",
    "too",
    "really",
    "extremely",
    "absolutely",
}

PUNCTUATION_TOKENS = {"!"}

# ---------------------------------------------------------------------
# Labeled dataset
# ---------------------------------------------------------------------

LABELED_POSTS = [
    # Positive
    ("I love this class so much", MoodLabel.POSITIVE),
    ("So excited for the weekend", MoodLabel.POSITIVE),
    ("This is actually pretty good!", MoodLabel.POSITIVE),
    ("I absolutely love getting stuck in traffic 😂", MoodLabel.POSITIVE),
    ("I am so excited!", MoodLabel.POSITIVE),
    ("That was really awesome!", MoodLabel.POSITIVE),
    ("This is amazing!", MoodLabel.POSITIVE),
    # Negative
    ("Today was a terrible day", MoodLabel.NEGATIVE),
    ("I am not happy about this", MoodLabel.NEGATIVE),
    ("This is so boring 😒", MoodLabel.NEGATIVE),
    ("I can't believe how much I hate this", MoodLabel.NEGATIVE),
    ("Uggh, 🙄", MoodLabel.NEGATIVE),
    ("Bruh 😭", MoodLabel.NEGATIVE),
    ("The food was not good", MoodLabel.NEGATIVE),
    ("Feeling very tired today", MoodLabel.NEGATIVE),
    ("This is absolutely awful", MoodLabel.NEGATIVE),
    ("I hate this so much!", MoodLabel.NEGATIVE),
    # Neutral
    ("This is fine", MoodLabel.NEUTRAL),
    ("Nothing special, just another day", MoodLabel.NEUTRAL),
    ("Say it isn't so", MoodLabel.NEUTRAL),
    ("I went to the store today", MoodLabel.NEUTRAL),
    # Mixed
    ("Feeling tired but kind of hopeful", MoodLabel.MIXED),
    ("Lowkey stressed but kind of proud of myself", MoodLabel.MIXED),
    ("Feeling a bit overwhelmed but managing", MoodLabel.MIXED),
    # Negation
    ("That exam was not bad at all", MoodLabel.POSITIVE),
    ("I am not really happy with how this went", MoodLabel.NEGATIVE),
    ("It was not exactly good but fine I guess", MoodLabel.NEUTRAL),
    # Negation + amplifier stacked
    ("I am not very happy about this", MoodLabel.NEGATIVE),
    ("It's not really bad though", MoodLabel.POSITIVE),
    # Edge cases
    ("I love the idea but I hate the execution", MoodLabel.NEUTRAL),
    ("Oh great, another meeting. Just what I needed.", MoodLabel.NEGATIVE),  # sarcasm
    ("I am not not happy", MoodLabel.POSITIVE),  # double negation
]
