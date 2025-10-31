import sys
import os

# Add the parent directory to the Python path to allow importing 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_hello():
    r = client.get("/hello/JC")
    assert r.status_code == 200
    assert r.json()["message"].startswith("Hello, JC")