import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex01_decorator import retry


def test_retry_success():
    """第一次就成功，不应重试"""
    call_count = 0

    @retry(max_retries=3)
    def succeed():
        nonlocal call_count
        call_count += 1
        return "ok"

    assert succeed() == "ok"
    assert call_count == 1


def test_retry_then_success():
    """前两次失败，第三次成功"""
    call_count = 0

    @retry(max_retries=3)
    def fail_then_succeed():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("fail")
        return "ok"

    assert fail_then_succeed() == "ok"
    assert call_count == 3


def test_retry_exhausted():
    """重试次数耗尽仍失败，应抛出异常"""
    @retry(max_retries=2)
    def always_fail():
        raise RuntimeError("always")

    with pytest.raises(RuntimeError, match="always"):
        always_fail()


def test_retry_specific_exception():
    """只捕获指定异常类型"""
    @retry(max_retries=3, exceptions=(ValueError,))
    def raise_type_error():
        raise TypeError("wrong type")

    with pytest.raises(TypeError):
        raise_type_error()
