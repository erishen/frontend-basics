import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex05_dependencies import app

client = TestClient(app)


def test_common_params():
    resp = client.get("/items/?q=hi&skip=5&limit=20")
    assert resp.status_code == 200
    assert resp.json() == {"q": "hi", "skip": 5, "limit": 20}
