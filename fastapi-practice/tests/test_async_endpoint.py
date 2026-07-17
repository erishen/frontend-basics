import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex10_async_endpoint import app

client = TestClient(app)


def test_async_doubled():
    resp = client.get("/async-items/21")
    assert resp.status_code == 200
    assert resp.json() == {"doubled": 42}
