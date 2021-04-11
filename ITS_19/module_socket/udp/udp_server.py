import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8300))
print('Server started')
result = s.recv(1024)
print(f'message from client: {result.decode("utf-8")}')
print('Server terminated')