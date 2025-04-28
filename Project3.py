import requests
import json

# Constants
API_KEY = 'your_api_key_here'  # Get your API key from OpenWeatherMap or WeatherAPI
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_weather_data(city_name):
    """ Fetch current weather data for a given city. """
    url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_data(city_name):
    """ Fetch 7-day weather forecast for a given city. """
    url = f"{BASE_URL}forecast/daily?q={city_name}&cnt=7&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather_info(city_name):
    """ Display current weather information for the given city. """
    data = get_weather_data(city_name)
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description']}")
    else:
        print(f"City {city_name} not found!")

def display_forecast_info(city_name):
    """ Display 7-day weather forecast for the given city. """
    forecast = get_forecast_data(city_name)
    if forecast["cod"] == "200":
        print(f"\n7-Day Weather Forecast for {city_name}:")
        for day in forecast['list']:
            print(f"Date: {day['dt_txt']} | Temp: {day['temp']['day']}°C | Weather: {day['weather'][0]['description']}")
    else:
        print(f"Unable to retrieve forecast for {city_name}.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_weather_info(city_name)
    display_forecast_info(city_name)
