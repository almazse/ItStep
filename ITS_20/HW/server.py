import socket
import json


class ChatServer:
    def __init__(self):

        self.client = []  # Массив где храним адреса клиентов

    def start_server(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.bind(('', 53210))
        serv_sock.listen(2)
        print('Start Server')
        while True:
            client_sock, client_addr = serv_sock.accept()
            print('Connected by', client_addr)
            try:
                if client_sock not in self.client:
                    self.client.append(client_sock)  # Если такого клиента нет, то добавить
                for clients in self.client:
                    data = clients.recv(1024)
                    if not data:
                        # Клиент отключился
                        print("Disconnect", client_addr)
            except KeyboardInterrupt:
                break

        print('Server terminated')


if __name__ == '__main__':
    server = ChatServer()
    server.start_server()
    