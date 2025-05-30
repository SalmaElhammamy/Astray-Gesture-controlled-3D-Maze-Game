import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Gesture Model API is live 🚀"}

def test_predict_valid_input():
    dummy_input = {
        "landmarks": [0.1] * 63  # Adjust this to match expected input size
    }
    response = client.post("/predict", json=dummy_input)
    assert response.status_code == 200
    json_data = response.json()
    assert "prediction" in json_data
    assert isinstance(json_data["prediction"], (int, str))  # Model might return label as int or str

def test_predict_invalid_input():
    # Input with incorrect length or invalid data
    invalid_input = {
        "landmarks": [0.1] * 10  # Too short if model expects 63
    }
    response = client.post("/predict", json=invalid_input)
    # Depending on your validation, this might return 422 or other error
    assert response.status_code == 422 or response.status_code == 400
