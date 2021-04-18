"""
format of connection request from client:
(
    "country": "Ukraine",
    "city": "Zaporizhia"
)
"""

import socket
import json
from dataclasses import dataclass


@dataclass
class WeatherToWeek:
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str


class WeatherServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', 8300))

    @staticmethod
    def _get_weather_by_country_and_city(self, country: str, city: str) -> {}:
        data_prettified = self._get_weather_data_from_json_file()
        try:
            weather_data = WeatherToWeek(**data_prettified[country][city])
        except KeyError:
            return {"error": 404, "message": "Country or city was not found"}
        return weather_data

    @staticmethod
    def _get_weather_data_from_json_file():
        data_prettified = {}
        with open("data.json") as file:
            data_row = file.readlines()
            data = "".join(data_row)
            data_prettified = json.loads(data)
        return data_prettified

    def start(self):
        print("Server was started.")
        while True:
            try:
                data, address = self.sock.recvfrom(1024)
                data_message = json.loads(data.decode('utf-8'))
                weather_data = self._get_weather_by_country_and_city(data_message["country"], data_message['city'])
                data_to_send = weather_data
                self.sock.sendto(weather_data, address)
            except KeyboardInterrupt:
                break
        print("Server was terminated.")