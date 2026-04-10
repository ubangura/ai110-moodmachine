import pytest
from mood_analyzer import MoodAnalyzer


@pytest.fixture
def analyzer():
    return MoodAnalyzer()


def test_returns_lowercase_tokens_when_simple_sentence(analyzer):
    assert analyzer.preprocess("Hello World") == ["hello", "world"]


def test_returns_empty_list_when_only_whitespace(analyzer):
    assert analyzer.preprocess("   ") == []


def test_returns_empty_list_when_only_nonsignificant_punctuation(analyzer):
    assert analyzer.preprocess("...,,,,") == []


def test_isolates_exclamation_when_exclamation_between_words(analyzer):
    assert analyzer.preprocess("wow! amazing") == ["wow", "!", "amazing"]


def test_keeps_only_exclamation_when_mixed_punctuation(analyzer):
    assert analyzer.preprocess("wait... what?!") == ["wait", "what", "!"]


def test_returns_alias_when_standalone_emoji(analyzer):
    assert analyzer.preprocess("😊") == ["happy"]


def test_splits_into_word_and_alias_when_emoji_glued_to_word(analyzer):
    assert analyzer.preprocess("good😊") == ["good", "happy"]


# ---------------------------------------------------------------------
# score_text
# ---------------------------------------------------------------------


def test_returns_positive_score_when_single_positive_word(analyzer):
    assert analyzer.score_text("happy") == 1


def test_accumulates_scores_when_multiple_sentiment_words(analyzer):
    assert analyzer.score_text("happy great") == 2


def test_returns_zero_when_positive_and_negative_cancel(analyzer):
    assert analyzer.score_text("love hate") == 0


def test_flips_sign_when_negation_before_positive_word(analyzer):
    assert analyzer.score_text("not happy") == -1


def test_flips_negative_to_positive_when_negation_before_negative_word(analyzer):
    assert analyzer.score_text("not bad") == 1


def test_doubles_magnitude_when_amplifier_before_positive_word(analyzer):
    assert analyzer.score_text("very happy") == 2


def test_doubles_negative_magnitude_when_amplifier_before_negative_word(analyzer):
    assert analyzer.score_text("very sad") == -2


def test_applies_both_modifiers_when_negation_and_amplifier_stacked(analyzer):
    assert analyzer.score_text("not very happy") == -2


def test_resets_flags_when_neutral_word_between_negation_and_sentiment(analyzer):
    assert analyzer.score_text("not something happy") == 1


def test_resets_flags_after_sentiment_word(analyzer):
    assert analyzer.score_text("not happy happy") == 0


def test_scores_exclamation_mark_as_positive(analyzer):
    assert analyzer.score_text("happy!") == 2


def test_returns_zero_when_no_sentiment_words(analyzer):
    assert analyzer.score_text("the quick brown fox") == 0


def test_returns_zero_when_only_modifiers(analyzer):
    assert analyzer.score_text("not very") == 0
