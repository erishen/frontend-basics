import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex08_binary_search import binary_search, find_first, find_last


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_empty():
    assert binary_search([], 1) == -1


def test_find_first():
    assert find_first([1, 2, 2, 2, 3, 4], 2) == 1


def test_find_last():
    assert find_last([1, 2, 2, 2, 3, 4], 2) == 3


def test_find_first_not_found():
    assert find_first([1, 3, 5], 2) == -1


def test_find_last_not_found():
    assert find_last([1, 3, 5], 2) == -1
