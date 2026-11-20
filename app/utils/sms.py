from twilio.rest import Client
import os

class SMSService:
    def __init__(self):
        self.twilio_sid = os.getenv("TWILIO_SID")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone = os.getenv("TWILIO_PHONE")
        self.client = Client(self.twilio_sid, self.twilio_auth_token)

    def send_sms(self, to: str, message: str):
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_phone,
            to=to
        )
        return message.sid

def send_alert(to: str, crop: str, price: float, unit: str):
    sms_service = SMSService()
    message = f"Alert: The price of {crop} is now {price} {unit}."
    return sms_service.send_sms(to, message)