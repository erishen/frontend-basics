import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex03_request_body import app

client = TestClient(app)


def test_create_item():
    resp = client.post("/items/", json={"name": "x", "price": 10.0})
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "x"
    assert data["price"] == 10.0
    assert data["id"] == 1
    assert data["tax"] is None
