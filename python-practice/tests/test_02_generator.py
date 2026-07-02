import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex02_generator import fibonacci, chunks, flatten_gen


def test_fibonacci_first_10():
    gen = fibonacci()
    result = [next(gen) for _ in range(10)]
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_chunks_even_split():
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunks_uneven():
    assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_chunks_larger_than_list():
    assert list(chunks([1, 2], 5)) == [[1, 2]]


def test_flatten_gen():
    assert list(flatten_gen([1, [2, [3, [4]]]])) == [1, 2, 3, 4]


def test_flatten_gen_mixed():
    assert list(flatten_gen([1, (2, 3), [4, (5, 6)]])) == [1, 2, 3, 4, 5, 6]
