"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional
import string

from dataset import (
    WORD_WEIGHTS,
    EMOJI_MAP,
    NEGATION_WORDS,
    AMPLIFIER_WORDS,
    PUNCTUATION_TOKENS,
    MoodLabel,
)


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        word_weights: Optional[Dict[str, int]] = None,
    ) -> None:
        self.word_weights = word_weights or WORD_WEIGHTS

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.
        """

        cleaned = text.strip().lower()

        expanded = ""
        for char in cleaned:
            if char in EMOJI_MAP:
                expanded += f" {EMOJI_MAP[char]} "
            elif char in PUNCTUATION_TOKENS:
                expanded += f" {char} "
            else:
                expanded += char

        tokens = []

        for token in expanded.split():
            if token in PUNCTUATION_TOKENS:
                tokens.append(token)
            else:
                stripped = "".join(c for c in token if c not in string.punctuation)
                if stripped:
                    tokens.append(stripped)

        print(f"Preprocessed '{text}' to {tokens}")
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.
        """
        score = 0
        negate_next, amplify_next = False, False

        for token in self.preprocess(text):
            if token in NEGATION_WORDS:
                negate_next = True
                continue
            if token in AMPLIFIER_WORDS:
                amplify_next = True
                continue

            token_score = self.word_weights.get(token, 0)
            if token_score:
                if amplify_next:
                    token_score *= 2
                if negate_next:
                    token_score = -token_score
                score += token_score

            negate_next = False
            amplify_next = False

        return score

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> MoodLabel:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> MoodLabel.POSITIVE
          - score < 0  -> MoodLabel.NEGATIVE
          - score == 0 -> MoodLabel.NEUTRAL

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be POSITIVE)
          - Add MoodLabel.MIXED for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in LABELED_POSTS in dataset.py if you care about accuracy.
        """
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return MoodLabel.POSITIVE if the score is above 0.
        #   3. Return MoodLabel.NEGATIVE if the score is below 0.
        #   4. Return MoodLabel.NEUTRAL otherwise.
        pass

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        tokens = self.preprocess(text)

        positive_hits: List[str] = []
        negative_hits: List[str] = []
        score = 0

        for token in tokens:
            if token in self.positive_words:
                positive_hits.append(token)
                score += 1
            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )


if __name__ == "__main__":
    analyzer = MoodAnalyzer()
    analyzer.preprocess("I love this class so much")
