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


def test_returns_all_aliases_when_consecutive_different_emojis(analyzer):
    assert analyzer.preprocess("😊😢😡😍") == ["happy", "sad", "angry", "love"]
