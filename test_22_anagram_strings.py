import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_valid_anagram():
    assert is_anagram("listen", "silent") == True


def test_invalid_anagram():
    assert is_anagram("hello", "world") == False


def test_uppercase_anagram():
    assert is_anagram("Listen", "Silent") == True


def test_anagram_with_spaces():
    assert is_anagram("rail safety", "fairy tales") == True


def test_empty_strings():
    assert is_anagram("", "") == True