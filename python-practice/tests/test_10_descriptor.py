import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.ex10_descriptor import TypeValidator, RangeValidator


def test_type_validator_pass():
    class Person:
        name = TypeValidator("name", str)
        age = TypeValidator("age", int)

    p = Person()
    p.name = "Lei"
    p.age = 30
    assert p.name == "Lei"
    assert p.age == 30


def test_type_validator_fail():
    class Person:
        name = TypeValidator("name", str)

    p = Person()
    with pytest.raises(TypeError, match="must be str"):
        p.name = 123


def test_range_validator_pass():
    class Config:
        port = RangeValidator("port", 1, 65535)

    c = Config()
    c.port = 8080
    assert c.port == 8080


def test_range_validator_fail():
    class Config:
        port = RangeValidator("port", 1, 65535)

    c = Config()
    with pytest.raises(ValueError, match="must be between"):
        c.port = 0

    with pytest.raises(ValueError, match="must be between"):
        c.port = 70000
