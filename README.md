# Crop Price AI Agent

This project is a FastAPI application designed to provide real-time crop price information and alerts to farmers. It utilizes LangChain for natural language processing and integrates with Twilio for SMS notifications.

## Project Structure

```
crop-price-agent/
├── README.md
├── requirements.txt
├── .env
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── ingestion/
│   │   ├── fetch_sources.py
│   │   ├── normalize_chain.py
│   │   └── validate.py
│   ├── logic/
│   │   ├── price_resolver.py
│   │   ├── alerts.py
│   │   └── messaging_chain.py
│   ├── api/
│   │   ├── routes_prices.py
│   │   ├── routes_subs.py
│   │   └── routes_admin.py
│   ├── agents/
│   │   ├── tools.py
│   │   └── farmer_agent.py
│   └── utils/
│       └── sms.py
└── tests/
    ├── test_ingestion.py
    ├── test_resolver.py
    ├── test_api.py
    └── test_agent.py
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd crop-price-agent
   ```

2. **Create a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add the following variables:
   ```
   OPENAI_API_KEY=sk-xxxx
   DATABASE_URL=postgresql://user:pass@localhost:5432/cropdb
   REDIS_URL=redis://localhost:6379/0
   TWILIO_SID=xxxx
   TWILIO_AUTH_TOKEN=xxxx
   TWILIO_PHONE=+1234567890
   ```

## Running the Application

To start the FastAPI server, run the following command:
```bash
uvicorn app.main:app --reload
```
You can access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Testing

Unit tests are located in the `tests/` directory. You can run the tests using:
```bash
pytest
```

## Next Steps

- Implement database models in `database.py`.
- Enhance the ingestion logic in `fetch_sources.py`.
- Integrate Twilio for SMS notifications in `utils/sms.py`.
- Expand the LangChain agent functionality in `agents/farmer_agent.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.