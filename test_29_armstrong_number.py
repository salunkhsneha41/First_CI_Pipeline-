import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_153():
    assert is_armstrong(153) == True


def test_armstrong_370():
    assert is_armstrong(370) == True


def test_armstrong_9474():
    assert is_armstrong(9474) == True


def test_non_armstrong_number():
    assert is_armstrong(123) == False


def test_negative_number():
    assert is_armstrong(-153) == False