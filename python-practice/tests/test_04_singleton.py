import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex04_singleton import Singleton, singleton_decorator


def test_singleton_new():
    a = Singleton("first")
    b = Singleton("second")
    assert a is b
    assert a.value == "first"  # 第二次 init 不应覆盖


def test_singleton_decorator():
    @singleton_decorator
    class DB:
        def __init__(self, url):
            self.url = url

    db1 = DB("url1")
    db2 = DB("url2")
    assert db1 is db2
    assert db1.url == "url1"
