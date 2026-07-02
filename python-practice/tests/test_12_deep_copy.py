import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex12_deep_copy import deep_copy


def test_deep_copy_dict():
    original = {"a": 1, "b": {"c": 2}}
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original
    assert copied["b"] is not original["b"]


def test_deep_copy_list():
    original = [1, [2, [3, 4]]]
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original
    assert copied[1] is not original[1]


def test_deep_copy_tuple():
    original = (1, [2, 3])
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original
    assert copied[1] is not original[1]


def test_deep_copy_set():
    original = {1, 2, 3}
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original


def test_deep_copy_primitives():
    assert deep_copy(42) == 42
    assert deep_copy("hello") == "hello"
    assert deep_copy(None) is None
    assert deep_copy(True) is True
