import tkinter as tk
import socket
import json


class TkWindowClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("weather App")
        self.root.minsize(400, 400)
        self._create_labels()
        self._create_entries()
        self.send_button = tk.Button(self.root, text="SEND", command=self.send_data, font="Victor Mono 14")
        self.send_button.grid(row=3, column=0, columnspawn=2, padx=10, pady=10)

    def _create_labels(self):
        tk.Label(self.root, text="SEND", font="Victor Mono 21") \
            .grid(row=0, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.root, text="Enter country", font="Victor Mono 21") \
            .grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        tk.Label(self.root, text="Enter city", font="Victor Mono 21") \
            .grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    def _create_entries(self):
        self.country_entry = tk.Entry(self.root, width=30, font="Victor Mono 14")
        self.country_entry.grid(row=1, column=1, padx=10, pady=10)

        self.city_entry = tk.Entry(self.root, width=30, font="Victor Mono 14")
        self.city_entry.grid(row=2, column=1, padx=10, pady=10)

    def send_data(self):
        pass


class WeatherClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tk_window = TkWindowClient()
        self.server = ('localhost', 8300)

    def read_socket(self):
        while True:
            try:
                data = self.socket.recv(1024)
                data_message = json.loads(data.decode('utf-8'))
                # ToDo call print results to tkinter
            except KeyboardInterrupt:
                break

    def send_to_server(self, message: dict):
        data_to_send = json.dumps(message)
        self.socket.sendto(data_to_send.encode('utf-8'), self.server)