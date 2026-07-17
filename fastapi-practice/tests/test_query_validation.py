import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex04_query_validation import app

client = TestClient(app)


def test_valid_limit():
    resp = client.get("/items/?limit=50")
    assert resp.status_code == 200
    assert resp.json() == {"skip": 0, "limit": 50}


def test_invalid_limit():
    resp = client.get("/items/?limit=200")
    assert resp.status_code == 422


def test_default_limit():
    resp = client.get("/items/")
    assert resp.status_code == 200
    assert resp.json() == {"skip": 0, "limit": 10}
