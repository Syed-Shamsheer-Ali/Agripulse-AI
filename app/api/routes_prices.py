from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/price")
def get_price(crop_id: int, market_id: int, region: str = None):
    # Dummy response — later query DB
    return {
        "crop_id": crop_id,
        "market_id": market_id,
        "region": region,
        "price": 2100,
        "unit": "quintal",
        "timestamp": datetime.now().isoformat()
    }