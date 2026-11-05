import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_empty_first_list():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_empty_second_list():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_empty():
    assert merge_sorted_lists([], []) == []


def test_duplicate_values():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]