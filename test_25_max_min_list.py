import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_positive_numbers():
    assert find_max_min([10, 20, 5, 30, 15]) == (30, 5)


def test_negative_numbers():
    assert find_max_min([-10, -20, -5, -30]) == (-5, -30)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([5, 5, 5, 5]) == (5, 5)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])