# main.py

from weather_api import WeatherAPI, WeatherHistory
from weather_forecast import WeatherForecast


def main():
    api_token = "013b692d1ef1446d985183317240607"  
    api = WeatherAPI(api_token)
    forecast_api = WeatherForecast(api_token)
    history_api = WeatherHistory(api_token)

    city = input("Enter city name: ")

    # Fetch current weather
    current_weather = api.get_weather(city)
    print(current_weather)

    # Fetch 3-day forecast
    forecast = forecast_api.get_forecast(city)
    print(forecast)

    # Fetch historical weather for a specific date
    date = input("Enter date (YYYY-MM-DD) for historical weather: ")
    historical_weather = history_api.get_history(city, date)
    print(historical_weather)


main()
