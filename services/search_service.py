# services/search_service.py

import requests
import os

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_entity(prompt):
    """Uses SerpAPI to get search results for the prompt."""
    try:
        params = {
            "engine": "google",
            "q": prompt,
            "api_key": SERPAPI_KEY
        }
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        search_results = response.json()
        # Extract only the necessary information
        return {
            "results": search_results.get("organic_results", [])
        }
    except Exception as e:
        print(f"Error fetching search results from SerpAPI: {e}")
        return {"results": []}  # Return empty results on error