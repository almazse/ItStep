import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import json
import threading


class ChatClient:

    def __init__(self, master):
        self.master = master
        self.font = "Arial 14"
        self.server = '127.0.0.1', 8300
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 0))  # Задаем сокет как клиент
        self.username = ''
        self.chat = ''
        self.message = ''
        master.title("Авторизация")
        master.minsize(250, 150)
        tk.Label(master, text="ENTER", font='Arial 20') \
            .grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(master, text="Enter login: ", font=self.font) \
            .grid(row=1, column=0, padx=5, pady=5)

        tk.Label(master, text="Enter password: ", font=self.font) \
            .grid(row=2, column=0, padx=5, pady=5)

        self.login_entry = tk.Entry(master, width=15, font=self.font)
        self.login_entry.grid(row=1, column=1, padx=5, pady=5)

        self.password_entry = tk.Entry(master, show="*", width=15, font=self.font)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        login_btn = tk.Button(master, text="login", command=self.login, font=self.font)
        login_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        master.bind('<Return>', self.login)

    def read_sok(self):
        while True:
            try:
                data = self.socket.recv(1024)
                data_msg = json.loads(data.decode('utf-8'))
                self.chat.insert(tk.INSERT, f'[{data_msg["login"]}]{data_msg["message"]}\n')
                self.chat.see("end")
            except KeyboardInterrupt:
                break

    def send_to_server(self, message):
        send_server = json.dumps(message)
        self.socket.sendto(send_server.encode('utf-8'), self.server)

    def send_msg(self, *args, **kwargs):
        data_message = {
            'action': "message",
            'login': self.username,
            'message': self.message.get(),
        }
        self.send_to_server(data_message)

    def login(self, *args):
        data_login = {
            'action': "login",
            'login': self.login_entry.get(),
            'password': self.password_entry.get(),
        }
        self.send_to_server(data_login)
        data = self.socket.recv(1024)
        if data.decode("utf-8") != "password":
            self.username = data.decode("utf-8")
            self.open_chat()
        else:
            tk.messagebox.showwarning("Error", "Incorrect login or password")

    def open_chat(self):
        self.master.destroy()
        window = tk.Tk()
        window.title("Добро пожаловать в чат")
        data_connect = {
            'action': "connect",
            'login': self.username,
            'message': "Connect to server",
        }
        connect_send = json.dumps(data_connect)
        self.socket.sendto(connect_send.encode('utf-8'), self.server)  # Уведомляем сервер о подключении

        self.chat = tk.scrolledtext.ScrolledText(window, width=80, height=10)
        self.chat.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        self.message = tk.Entry(window, width=40, font=self.font)
        self.message.grid(column=0, row=1, padx=5, pady=5)

        send_btn = tk.Button(window, width=20, text="Send", font="Arial 12")
        send_btn.grid(column=1, row=1, padx=5, pady=5)
        send_btn.config(command=self.send_msg)

        window.bind('<Return>', self.send_msg)

        thread = threading.Thread(target=self.read_sok)
        thread.start()

        window.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    chat = ChatClient(root)
    root.mainloop()

