import socket
import json


class ChatServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', 8300))
        # База пользователей ['логин', 'пароль']
        self.users = [
            ['kirill', '123'],
            ['oleg', '123123'],
            ['andrey', '123321'],
        ]
        self.client = []  # Массив где храним адреса клиентов

    def start_server(self):
        print('Start Server')
        while True:
            try:
                data, address = self.sock.recvfrom(1024)
                print(address[0], address[1], data.decode("utf-8"))
                data_msg = json.loads(data.decode('utf-8'))
                if data_msg['action'] == "login":
                    if [data_msg['login'], data_msg['password']] in self.users:
                        self.sock.sendto(data_msg['login'].encode('utf-8'), address)
                    else:
                        self.sock.sendto("password".encode('utf-8'), address)
                else:
                    if address not in self.client:
                        self.client.append(address)  # Если такого клиента нет, то добавить
                    for clients in self.client:
                        self.sock.sendto(data, clients)
            except KeyboardInterrupt:
                break

        print('Server terminated')


if __name__ == '__main__':
    server = ChatServer()
    server.start_server()
