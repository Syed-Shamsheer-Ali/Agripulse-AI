from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_farmer_agent_response():
    response = client.get("/api/price?crop_id=1&market_id=1")
    assert response.status_code == 200
    assert "price" in response.json()
    assert "unit" in response.json()

def test_subscription_endpoint():
    response = client.post("/api/subscribe", json={"phone": "+1234567890", "crop_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Subscription successful."}