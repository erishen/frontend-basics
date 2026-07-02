import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex06_flatten import flatten, flatten_iter


def test_flatten_deep():
    assert flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_flatten_with_tuples():
    assert flatten([1, (2, 3), [4, (5, 6)]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_empty():
    assert flatten([]) == []
    assert flatten([[], [[]], []]) == []


def test_flatten_iter_deep():
    assert flatten_iter([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_flatten_iter_empty():
    assert flatten_iter([]) == []
