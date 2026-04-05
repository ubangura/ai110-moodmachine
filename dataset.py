"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter set of positive words
  - NEGATIVE_WORDS: starter set of negative words
  - LABELED_POSTS: list of (post, true_label) tuples for evaluation and training
"""

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

# Each entry is a (post, true_label) tuple.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
LABELED_POSTS = [
    ("I love this class so much",                       "positive"),
    ("Today was a terrible day",                        "negative"),
    ("Feeling tired but kind of hopeful",               "mixed"),
    ("This is fine",                                    "neutral"),
    ("So excited for the weekend",                      "positive"),
    ("I am not happy about this",                       "negative"),
    ("Lowkey stressed but kind of proud of myself",     "mixed"),
    ("This is so boring 😒",                            "negative"),
    ("I can't believe how much I hate this",            "negative"),
    ("I absolutely love getting stuck in traffic 😂",   "positive"),
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - Each entry must be a (post, true_label) tuple.
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
# LABELED_POSTS.append(("Lowkey stressed but kind of proud of myself", "mixed"))
