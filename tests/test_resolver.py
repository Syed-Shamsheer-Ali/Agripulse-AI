from app.logic.price_resolver import compute_authoritative_price
import pytest

def test_compute_authoritative_price():
    prices = [
        {"price_value": 100},
        {"price_value": 200},
        {"price_value": 300},
        {"price_value": 400},
        {"price_value": 500},
    ]
    average_price, method = compute_authoritative_price(prices)
    assert average_price == 300
    assert method == "median_outlier_rejection"

def test_compute_authoritative_price_with_outliers():
    prices = [
        {"price_value": 100},
        {"price_value": 200},
        {"price_value": 300},
        {"price_value": 1000},  # Outlier
        {"price_value": 500},
    ]
    average_price, method = compute_authoritative_price(prices)
    assert average_price == 300
    assert method == "median_outlier_rejection"

def test_compute_authoritative_price_empty():
    prices = []
    with pytest.raises(ZeroDivisionError):
        compute_authoritative_price(prices)