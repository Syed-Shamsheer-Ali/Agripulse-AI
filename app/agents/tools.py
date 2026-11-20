from langchain.tools import Tool

def fetch_crop_prices_tool():
    return Tool(
        name="fetch_crop_prices",
        description="Fetches the latest crop prices from various sources.",
        func=fetch_crop_prices,
    )

def fetch_crop_prices():
    """
    Fetches the latest crop prices from a mock API or database.
    Replace this logic with real API/database calls as needed.
    """
    # Example: Simulate fetching from an API or DB
    # In production, use requests.get() or a DB query here
    crop_prices = [
        {
            "crop_name": "Wheat",
            "market_name": "Delhi",
            "region": "North",
            "price_value": 2100,
            "price_unit": "quintal",
            "timestamp": "2025-09-13T10:00:00",
            "source_id": "mock_api"
        },
        {
            "crop_name": "Rice",
            "market_name": "Mumbai",
            "region": "West",
            "price_value": 1800,
            "price_unit": "quintal",
            "timestamp": "2025-09-13T10:00:00",
            "source_id": "mock_api"
        }
    ]
    return crop_prices

def normalize_crop_data_tool():
    return Tool(
        name="normalize_crop_data",
        description="Normalizes raw crop data into a structured format.",
        func=normalize_crop_data,
    )

def normalize_crop_data(raw_data):
    """
    Normalizes raw crop data into a structured format.
    Expects raw_data as a list of dicts or a raw string (JSON or CSV).
    Returns a list of dicts with keys:
    crop_name, market_name, region, price_value, price_unit, timestamp, source_id
    """
    import json

    # If raw_data is a string, try to parse as JSON
    if isinstance(raw_data, str):
        try:
            data = json.loads(raw_data)
        except Exception:
            # If not JSON, return empty list or handle CSV/other formats as needed
            return []
    elif isinstance(raw_data, list):
        data = raw_data
    else:
        return []

    normalized = []
    for entry in data:
        normalized.append({
            "crop_name": entry.get("crop_name", "").strip(),
            "market_name": entry.get("market_name", "").strip(),
            "region": entry.get("region", "").strip(),
            "price_value": float(entry.get("price_value", 0)),
            "price_unit": entry.get("price_unit", "").strip(),
            "timestamp": entry.get("timestamp", ""),
            "source_id": entry.get("source_id", "unknown")
        })
    return normalized

def send_alert_tool():
    return Tool(
        name="send_alert",
        description="Sends alerts based on price changes.",
        func=send_alert,
    )

def send_alert(alert_message):
    """
    Sends alerts (e.g., via SMS or email).
    Replace this logic with integration to Twilio, email, or other services.
    """
    # Example: Print to console (replace with real SMS/email logic)
    print(f"ALERT: {alert_message}")
    return {"status": "sent", "message": alert_message}

# Additional tools can be defined here as needed.

if __name__ == "__main__":
    print("Testing fetch_crop_prices:")
    prices = fetch_crop_prices()
    print(prices)

    print("\nTesting normalize_crop_data:")
    normalized = normalize_crop_data(prices)
    print(normalized)

    print("\nTesting send_alert:")
    result = send_alert("Test alert: Price threshold reached!")
    print(result)