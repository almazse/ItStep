"""
format of connection request from client:
(
    "country": "Ukraine",
    "city": "Zaporizhia"
)
"""

import socket
import json
from pydantic import BaseModel
from typing import List, Optional
import datetime


class WeatherToWeek(BaseModel):
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str


class ResponseError(BaseModel):
    error: int
    message: str


class Response(BaseModel):
    errors: Optional[List[ResponseError]]
    data: Optional[WeatherToWeek]


class WeatherServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('localhost', 8300))

    def _get_weather_by_country_and_city(self, country: str, city: str) -> Response:
        data_prettified = self._get_weather_data_from_json_file()
        try:
            weather_data = WeatherToWeek(**data_prettified[country][city])
        except KeyError:
            response_error = ResponseError(error=404, message="Country or city was not found")
            return Response(errors=[response_error])
        return Response(data=weather_data)

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
                data_to_send = weather_data.json().encode('utf-8')
                self.sock.sendto(data_to_send, address)
                print(f'[{datetime.datetime.now()}] weather data was sent to -> {address}')
            except KeyboardInterrupt:
                break
        print("Server was terminated.")


if __name__ == '__main__':
    weather_app_server = WeatherServer()
    weather_app_server.start()
