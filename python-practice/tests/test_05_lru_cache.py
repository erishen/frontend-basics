import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex05_lru_cache import LRUCache


def test_basic_get_put():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    assert cache.get(2) == 2


def test_eviction():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)  # 淘汰 key=1
    assert cache.get(1) == -1
    assert cache.get(3) == 3


def test_get_refreshes():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      # 刷新 key=1
    cache.put(3, 3)   # 淘汰 key=2
    assert cache.get(2) == -1
    assert cache.get(1) == 1


def test_update_existing():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 10)
    assert cache.get(1) == 10
