import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex12_cors import app

client = TestClient(app)


def test_cors_header():
    resp = client.get("/", headers={"Origin": "http://example.com"})
    assert resp.status_code == 200
    assert resp.headers.get("access-control-allow-origin") == "*"
