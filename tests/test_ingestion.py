from fastapi import HTTPException
import pytest
from app.ingestion.normalize_chain import normalize_feed

def test_normalize_feed_valid_data():
    raw_data = "Sample raw data with crop price information."
    expected_output = {
        "crop_name": "Sample Crop",
        "market_name": "Sample Market",
        "region": "Sample Region",
        "price_value": 100,
        "price_unit": "quintal",
        "timestamp": "2023-10-01T12:00:00",
        "source_id": "source_1"
    }
    result = normalize_feed(raw_data)
    assert result == expected_output

def test_normalize_feed_invalid_data():
    raw_data = ""
    with pytest.raises(HTTPException):
        normalize_feed(raw_data)

def test_normalize_feed_outlier_data():
    raw_data = "Outlier data that should be filtered out."
    expected_output = {
        "crop_name": "Outlier Crop",
        "market_name": "Outlier Market",
        "region": "Outlier Region",
        "price_value": 2000,
        "price_unit": "quintal",
        "timestamp": "2023-10-01T12:00:00",
        "source_id": "source_2"
    }
    result = normalize_feed(raw_data)
    assert result == expected_output