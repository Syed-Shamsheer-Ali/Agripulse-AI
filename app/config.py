from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()  # Load environment variables from .env file

    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "REDIS_URL": os.getenv("REDIS_URL"),
        "TWILIO_SID": os.getenv("TWILIO_SID"),
        "TWILIO_AUTH_TOKEN": os.getenv("TWILIO_AUTH_TOKEN"),
        "TWILIO_PHONE": os.getenv("TWILIO_PHONE"),
    }