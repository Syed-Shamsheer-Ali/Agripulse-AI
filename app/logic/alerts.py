from typing import List, Dict

class PriceAlert:
    def __init__(self, threshold: float):
        self.threshold = threshold
        self.previous_price = None

    def check_alert(self, current_price: float) -> Dict[str, float]:
        if self.previous_price is None:
            self.previous_price = current_price
            return {}

        price_change = current_price - self.previous_price
        alert = {}

        if abs(price_change) >= self.threshold:
            alert = {
                "previous_price": self.previous_price,
                "current_price": current_price,
                "change": price_change,
                "alert": "Price change exceeds threshold"
            }

        self.previous_price = current_price
        return alert

def create_alerts(prices: List[float], threshold: float) -> List[Dict[str, float]]:
    alerts = []
    price_alert = PriceAlert(threshold)

    for price in prices:
        alert = price_alert.check_alert(price)
        if alert:
            alerts.append(alert)

    return alerts