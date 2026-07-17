import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex07_middleware import app

client = TestClient(app)


def test_header_added():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.headers.get("X-App-Name") == "fastapi-practice"
