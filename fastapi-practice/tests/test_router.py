import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex11_router import app

client = TestClient(app)


def test_list_users():
    resp = client.get("/users/")
    assert resp.status_code == 200
    assert resp.json() == ["alice", "bob"]


def test_get_user():
    resp = client.get("/users/3")
    assert resp.status_code == 200
    assert resp.json() == {"user_id": 3}
