import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_normal_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_same_sets():
    assert set_intersection({1, 2}, {1, 2}) == {1, 2}


def test_empty_first_set():
    assert set_intersection(set(), {1, 2}) == set()


def test_empty_second_set():
    assert set_intersection({1, 2}, set()) == set()