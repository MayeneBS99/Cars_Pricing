from fastapi.testclient import TestClient
from src.API.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de prédiction du prix des voitures"}

def test_predict():
    sample_data = {
        "mileage": 15.0,
        "engine": 1200,
        "power": 85.0,
        "fuel_type": "Petrol",
        "transmission": "Manual"
    }
    response = client.post("/predict/", json=sample_data)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
