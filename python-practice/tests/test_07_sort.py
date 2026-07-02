import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex07_sort import quick_sort, merge_sort, heap_sort


@pytest.mark.parametrize("sort_fn", [quick_sort, merge_sort, heap_sort])
class TestAllSorts:
    def test_normal(self, sort_fn):
        assert sort_fn([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]

    def test_empty(self, sort_fn):
        assert sort_fn([]) == []

    def test_single(self, sort_fn):
        assert sort_fn([1]) == [1]

    def test_sorted(self, sort_fn):
        assert sort_fn([1, 2, 3]) == [1, 2, 3]

    def test_reverse(self, sort_fn):
        assert sort_fn([3, 2, 1]) == [1, 2, 3]

    def test_duplicates(self, sort_fn):
        assert sort_fn([5, 5, 5, 5]) == [5, 5, 5, 5]

    def test_negative(self, sort_fn):
        assert sort_fn([-3, -1, -2, 0, 2]) == [-3, -2, -1, 0, 2]
