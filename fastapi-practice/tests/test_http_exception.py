import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex06_http_exception import app

client = TestClient(app)


def test_existing():
    resp = client.get("/items/1")
    assert resp.status_code == 200
    assert resp.json() == "foo"


def test_missing():
    resp = client.get("/items/999")
    assert resp.status_code == 404
