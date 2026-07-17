import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from fastapi.testclient import TestClient
from src.ex09_background_tasks import app, notifications

client = TestClient(app)


def test_background_task():
    resp = client.post("/send-notification/?email=a@b.com")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "Notification sent"}
    assert "a@b.com" in notifications
