import json

import requests
from typing import List

API_KEY = "79dd8ea1da14d54d5e9b1374621dbfcd"
API_BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_16_daily_forecast_data_by_city(city) -> List[float]:
    """
    Get forecast for 16 days for city.
    An prepare it to list float values of celsius degree
    Read more: https://openweathermap.org/forecast16
    :param city
    :return: [15, 25, 16, 12, 15, 25, 16,
              12, 15, 25, 16, 12, 15, 25,
              16, 12]

    """

    forecast_16_days_url = f'?q={city}&appid={API_KEY}'
    response = requests.post(f"{API_BASE_URL}{forecast_16_days_url}")
    return []


def get_current_weather(city: str) -> str:
    """
    Get current temperature by city celsius
    Args:
        city: "London"

    Returns: 12.0
    """
    current_temperature_url = f"weather"
    response = requests.post(f"{API_BASE_URL}{current_temperature_url}", params={"q": city, "appid": API_KEY})
    if response.status_code == 200:
        return json.load()


print(get_current_weather('Kyiv'))


