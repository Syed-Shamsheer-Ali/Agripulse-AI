from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Subscription(BaseModel):
    phone_number: str
    crop_id: int
    market_id: int

subscriptions = []

@router.post("/subscribe")
def subscribe(subscription: Subscription):
    if subscription.phone_number in [sub.phone_number for sub in subscriptions]:
        raise HTTPException(status_code=400, detail="Already subscribed")
    subscriptions.append(subscription)
    return {"message": "Subscription successful", "subscription": subscription}

@router.get("/subscriptions")
def get_subscriptions():
    return subscriptions

@router.delete("/unsubscribe/{phone_number}")
def unsubscribe(phone_number: str):
    global subscriptions
    subscriptions = [sub for sub in subscriptions if sub.phone_number != phone_number]
    return {"message": "Unsubscription successful"}