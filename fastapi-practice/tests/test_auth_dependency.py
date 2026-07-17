import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex08_auth_dependency import app

client = TestClient(app)


def test_with_key():
    resp = client.get("/secure/", headers={"X-API-Key": "secret"})
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_without_key():
    resp = client.get("/secure/")
    assert resp.status_code == 403
