from typing import List
import requests

def fetch_data_from_api(api_url: str) -> List[dict]:
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def fetch_data_from_web(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

def fetch_sources() -> List[dict]:
    api_urls = [
        "https://api.example.com/crop-prices",
        "https://api.example.com/market-data"
    ]
    
    raw_data = []
    for url in api_urls:
        try:
            data = fetch_data_from_api(url)
            raw_data.extend(data)
        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
    
    # Add web scraping logic if needed
    # Example: raw_html = fetch_data_from_web("https://example.com/some-page")
    
    return raw_data