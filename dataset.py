"""
Shared data for the Mood Machine lab.

This file defines:
  - MoodLabel: enum of allowed mood labels
  - POSITIVE_WORDS: starter set of positive words
  - NEGATIVE_WORDS: starter set of negative words
  - LABELED_POSTS: list of (post, MoodLabel) tuples for evaluation and training
"""

from enum import Enum


class MoodLabel(str, Enum):
    """Allowed mood labels for the Mood Machine."""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL  = "neutral"
    MIXED    = "mixed"


# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = {
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
}

NEGATIVE_WORDS = {
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
}

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Each entry is a (post, MoodLabel) tuple.
LABELED_POSTS = [
    ("I love this class so much",                       MoodLabel.POSITIVE),
    ("Today was a terrible day",                        MoodLabel.NEGATIVE),
    ("Feeling tired but kind of hopeful",               MoodLabel.MIXED),
    ("This is fine",                                    MoodLabel.NEUTRAL),
    ("So excited for the weekend",                      MoodLabel.POSITIVE),
    ("I am not happy about this",                       MoodLabel.NEGATIVE),
    ("Lowkey stressed but kind of proud of myself",     MoodLabel.MIXED),
    ("This is so boring 😒",                            MoodLabel.NEGATIVE),
    ("I can't believe how much I hate this",            MoodLabel.NEGATIVE),
    ("I absolutely love getting stuck in traffic 😂",   MoodLabel.POSITIVE),
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - Each entry must be a (post, MoodLabel) tuple.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the list:
#
# LABELED_POSTS.append(("Lowkey stressed but kind of proud of myself", MoodLabel.MIXED))
