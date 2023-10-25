from ..src.stop_words import stopWords
import pytest


def test_stop_word_1():
    text = "the quick brown fox jumps over the lazy brown dog and runs away to a brown house"
    k = 2
    words = stopWords(text, k)
    assert words == ["the", "brown"]


def test_stop_word_2():
    text = "foo bar foo baz foo"
    k = 3
    words = stopWords(text, k)
    assert words == ["foo"]


def test_stop_word_3():
    text = "foo bar foo baz foo"
    k = 1
    words = stopWords(text, k)
    assert words == ["foo", "bar", "baz"]
