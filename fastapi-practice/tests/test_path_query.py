import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex02_path_query import app

client = TestClient(app)


def test_with_query():
    resp = client.get("/items/42?q=abc")
    assert resp.status_code == 200
    assert resp.json() == {"item_id": 42, "q": "abc"}


def test_without_query():
    resp = client.get("/items/7")
    assert resp.status_code == 200
    assert resp.json() == {"item_id": 7, "q": None}
