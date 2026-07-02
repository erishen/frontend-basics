import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex11_coroutine import consumer, producer


def test_consumer_basic():
    c = consumer()
    next(c)  # 启动
    result = c.send(5)
    assert result == 10


def test_producer():
    c = consumer()
    results = producer(c, [1, 2, 3, 4, 5])
    assert results == [2, 4, 6, 8, 10]
