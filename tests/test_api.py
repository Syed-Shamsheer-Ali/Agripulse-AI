from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_price():
    response = client.get("/api/price?crop_id=1&market_id=1")
    assert response.status_code == 200
    assert "crop_id" in response.json()
    assert "market_id" in response.json()
    assert "price" in response.json()
    assert "unit" in response.json()

def test_get_price_with_region():
    response = client.get("/api/price?crop_id=1&market_id=1&region=North")
    assert response.status_code == 200
    assert response.json()["region"] == "North"

def test_get_price_invalid_crop_id():
    response = client.get("/api/price?crop_id=999&market_id=1")
    assert response.status_code == 404  # Assuming this returns a 404 for invalid crop_id

def test_get_price_invalid_market_id():
    response = client.get("/api/price?crop_id=1&market_id=999")
    assert response.status_code == 404  # Assuming this returns a 404 for invalid market_id

# Add others as needed (sqlalchemy, redis, twilio, etc.)