import requests

class WeatherAPI:
    def __init__(self, api_token):
        self.base_url = "http://api.weatherapi.com/v1"
        self.api_token = api_token

    def get_weather(self, city):
        endpoint = f"{self.base_url}/current.json"
        params = {
            "key": self.api_token,
            "q": city,
            "aqi": "no"  # Optional: Include air quality index
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            return f"Current weather in {city}: {condition}, Temperature: {temp_c}°C"
        else:
            return f"Failed to fetch weather data for {city}"

class WeatherHistory(WeatherAPI):
    def get_history(self, city, date):
        endpoint = f"{self.base_url}/history.json"
        params = {
            "key": self.api_token,
            "q": city,
            "dt": date  # Format: YYYY-MM-DD
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            max_temp = data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
            min_temp = data["forecast"]["forecastday"][0]["day"]["mintemp_c"]
            condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
            return f"Weather on {date} in {city}: Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Condition: {condition}"
        else:
            return f"Failed to fetch weather history for {city} on {date}"
