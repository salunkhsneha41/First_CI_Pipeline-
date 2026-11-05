import importlib

module = importlib.import_module("21_largest_word")
largest_word = module.largest_word


def test_normal_sentence():
    assert largest_word("Python is very powerful") == "powerful"


def test_single_word():
    assert largest_word("Hello") == "Hello"


def test_empty_string():
    assert largest_word("") == ""


def test_multiple_words():
    assert largest_word("I love programming") == "programming"


def test_equal_length_words():
    assert largest_word("cat dog") == "cat"