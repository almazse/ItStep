import tkinter as tk
import socket
import threading
import json

from view import TicTacToeView
from model import TicTacToeModel


class TicTacToeController:

    def __init__(self):
        self.root = tk.Tk()
        self.model = TicTacToeModel()
        self.view = TicTacToeView(self.root)
        self.server = ('127.0.0.1', 53210)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.socket.connect(self.server)

    def run(self):
        thread = threading.Thread(target=self.connect_to_server)
        thread.start()

        rectangle = self.model.RECTANGLE
        font = self.model.FONT
        # create window
        self.view.create_window(self.model.WIDTH, self.model.HEIGHT,
                                self.model.HEADER_S, rectangle)
        # create playground
        for row in range(3):
            for col in range(3):
                self.view.generate_playground(row, col, rectangle)

        # generate statistic
        self.view.generate_statistic(rectangle, self.model.COLOR, font)

        # generate restart button
        self.view.generate_restart_btn(rectangle, font)

        self.root.mainloop()
