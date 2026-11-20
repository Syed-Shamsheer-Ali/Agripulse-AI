from typing import List, Dict

def validate_price_data(prices: List[Dict]) -> bool:
    if not prices:
        return False
    
    for price in prices:
        if not isinstance(price.get("price_value"), (int, float)):
            return False
        if price.get("price_value") < 0:
            return False
        if not isinstance(price.get("timestamp"), str):
            return False
    
    return True

def validate_crop_data(crop_data: Dict) -> bool:
    required_keys = ["crop_name", "market_name", "region", "price_value", "price_unit", "timestamp", "source_id"]
    return all(key in crop_data for key in required_keys) and isinstance(crop_data["price_value"], (int, float)) and crop_data["price_value"] >= 0