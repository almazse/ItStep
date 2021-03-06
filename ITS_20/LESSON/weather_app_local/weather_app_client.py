import tkinter as tk
from threading import Thread
import socket
import json


class TkWindowClient:
    def __init__(self, send_func):
        self.root = tk.Tk()
        self.root.title("weather App")
        self.root.minsize(400, 800)
        self._create_labels()
        self._create_entries()
        self._send_outer_func = send_func
        self.send_button = tk.Button(self.root, text="SEND", command=self.send, font="Victor 14")
        self.send_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def _create_labels(self):
        tk.Label(self.root, text="Get weather", font="Victor 21") \
            .grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.root, text="Enter country", font="Victor 21") \
            .grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.root, text="Enter city", font="Victor 21") \
            .grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    def _create_entries(self):
        self.country_entry = tk.Entry(self.root, width=30, font="Victor 14")
        self.country_entry.grid(row=1, column=1, padx=10, pady=10)

        self.city_entry = tk.Entry(self.root, width=30, font="Victor 14")
        self.city_entry.grid(row=2, column=1, padx=10, pady=10)

    def send(self):
        self._send_outer_func(self.data_to_send)

    @property
    def data_to_send(self):
        return {
            "country": self.country_entry.get(),
            "city": self.city_entry.get()
        }

    def draw_results(self, result: dict):
        if result.get("errors"):
            self._draw_error_label(result['errors'][0])
        else:
            self._draw_weather_result(result['date'])

    def _draw_weather_result(self, weather_data: dict):
        row = 4
        for day, weather_value in weather_data.items():
            tk.Label(self.root, text=f'{day}: ', font="Victor 21", color="grey") \
                .grid(row=row, column=0, columnspan=2, padx=20, pady=20)
            tk.Label(self.root, text=weather_value, font="Victor 21", color="gold") \
                .grid(row=row, column=1, columnspan=2, padx=20, pady=20)
            row += 1

    def _draw_error_label(self, error_msg):
        tk.Label(self.root, text=error_msg, font="Victor 21", color="red") \
            .grid(row=4, column=0, columnspan=2, padx=20, pady=20)


class WeatherClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server = ('localhost', 8300)
        self.socket.bind(('', 8300))
        self.tk_window = TkWindowClient(self.send_to_server)
        self.thread = Thread(target=self.read_socket)
        self.thread.start()

    def read_socket(self):
        while True:
            try:
                data = self.socket.recv(1024)
                data_message = json.loads(data.decode('utf-8'))
                self.tk_window.draw_results(data_message)
            except KeyboardInterrupt:
                break

    def send_to_server(self, data):
        data_to_send = json.dumps(data)
        self.socket.sendto(data_to_send.encode('utf-8'), self.server)


if __name__ == '__main__':
    weather_app = WeatherClient()
    weather_app.tk_window.root.mainloop()
