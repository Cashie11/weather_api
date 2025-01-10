import requests
from django.core.cache import cache

# def get_weather_data(city):
#     api_key = "f8fff5212f1d7d12c04ca25ef93d6864"
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key, "units": "metric"}
#     response = requests.get(base_url, params=params)
#     return response.json()

import requests

def get_weather_data(city):
    api_key = "f8fff5212f1d7d12c04ca25ef93d6864"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return {"success": True, "data": response.json()}
    except requests.exceptions.HTTPError as http_err:
        return {"success": False, "error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"success": False, "error": f"Request error occurred: {req_err}"}

# def get_weather_data(city):
#     cached_data = cache.get(city)  # Check if data is cached
#     if cached_data:
#         return {"success": True, "data": cached_data}
    
#     api_key = "your_actual_api_key"
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key, "units": "metric"}
    
#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         cache.set(city, data, timeout=3600)  # Cache for 1 hour
#         return {"success": True, "data": data}
#     except requests.exceptions.RequestException as e:
#         return {"success": False, "error": str(e)}