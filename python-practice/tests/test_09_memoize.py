import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex09_memoize import memoize


def test_memoize_basic():
    call_count = 0

    @memoize
    def add(a, b):
        nonlocal call_count
        call_count += 1
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3  # 缓存命中
    assert call_count == 1  # 只调用了一次

    assert add(3, 4) == 7
    assert call_count == 2  # 新参数，调用两次


def test_memoize_kwargs():
    @memoize
    def greet(name, prefix="Hello"):
        return f"{prefix}, {name}"

    assert greet("Lei") == "Hello, Lei"
    assert greet("Lei") == "Hello, Lei"  # 缓存命中
    assert greet("Lei", prefix="Hi") == "Hi, Lei"  # 不同 kwargs


def test_memoize_fibonacci():
    @memoize
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(30) == 832040  # 不缓存会非常慢
