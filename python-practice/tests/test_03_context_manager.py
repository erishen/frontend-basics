import pytest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex03_context_manager import Timer, temp_attr


def test_timer():
    with Timer() as t:
        time.sleep(0.05)
    assert t.elapsed is not None
    assert t.elapsed >= 0.04


def test_temp_attr():
    class Config:
        debug = False

    config = Config()
    assert config.debug is False

    with temp_attr(config, "debug", True):
        assert config.debug is True

    assert config.debug is False


def test_temp_attr_restores_on_exception():
    class Config:
        value = "original"

    config = Config()
    try:
        with temp_attr(config, "value", "temp"):
            assert config.value == "temp"
            raise RuntimeError("oops")
    except RuntimeError:
        pass

    assert config.value == "original"
