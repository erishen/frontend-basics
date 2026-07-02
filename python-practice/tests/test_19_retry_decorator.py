import time
from unittest.mock import patch
from src.ex19_retry_decorator import retry


def test_success_first_try():
    call_count = 0

    @retry(max_retries=3, base_delay=0.01)
    def succeed():
        nonlocal call_count
        call_count += 1
        return "ok"

    assert succeed() == "ok"
    assert call_count == 1


def test_retry_then_succeed():
    call_count = 0

    @retry(max_retries=3, base_delay=0.01)
    def fail_twice():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("fail")
        return "ok"

    assert fail_twice() == "ok"
    assert call_count == 3


def test_max_retries_exceeded():
    @retry(max_retries=2, base_delay=0.01)
    def always_fail():
        raise RuntimeError("always")

    try:
        always_fail()
        assert False, "should have raised"
    except RuntimeError as e:
        assert str(e) == "always"


def test_only_catches_specified_exceptions():
    call_count = 0

    @retry(max_retries=3, base_delay=0.01, exceptions=(ValueError,))
    def raise_type_error():
        nonlocal call_count
        call_count += 1
        raise TypeError("wrong type")

    try:
        raise_type_error()
    except TypeError:
        pass
    assert call_count == 1  # 不重试 TypeError


@patch("src.ex19_retry_decorator.time.sleep")
def test_exponential_backoff(mock_sleep):
    call_count = 0

    @retry(max_retries=3, base_delay=1.0)
    def fail_then_succeed():
        nonlocal call_count
        call_count += 1
        if call_count <= 3:
            raise ValueError("fail")
        return "ok"

    fail_then_succeed()
    # 失败3次: 第1次重试等 1.0s, 第2次等 2.0s, 第3次等 4.0s
    assert mock_sleep.call_count == 3
    mock_sleep.assert_any_call(1.0)
    mock_sleep.assert_any_call(2.0)
    mock_sleep.assert_any_call(4.0)
