import requests
from weather_api import WeatherAPI

class WeatherForecast(WeatherAPI):
    def get_forecast(self, city, days=3):
        endpoint = f"{self.base_url}/forecast.json"
        params = {
            "key": self.api_token,
            "q": city,
            "days": days,
            "aqi": "no"  # Optional: Include air quality index
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            forecast = data["forecast"]["forecastday"]
            forecast_text = f"3-Day Weather Forecast for {city}:\n"
            for day in forecast:
                date = day["date"]
                max_temp = day["day"]["maxtemp_c"]
                min_temp = day["day"]["mintemp_c"]
                condition = day["day"]["condition"]["text"]
                forecast_text += f"{date}: Max Temp: {max_temp}°C, Min Temp: {min_temp}°C, Condition: {condition}\n"
            return forecast_text
        else:
            return f"Failed to fetch weather forecast for {city}"
