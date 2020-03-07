import requests
import pprint
from accounts import openweather_api_key

def get_current_weather(city):
    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?APPID='+ openweather_api_key +' &q='+ city + ',us').json()
    print(weather)
    # TODO: Parse this data


def get_weather_forecast(city):
    weather = requests.get('https://api.openweathermap.org/data/2.5/forecast?APPID='+ openweather_api_key +'&q='+ city + ',us').json()
    print(weather)

