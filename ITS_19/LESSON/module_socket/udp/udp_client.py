import socket

message = input('your message to server: ')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result = s.sendto(message.encode('utf-8'), ('127.0.0.1', 8300))
print('Message was send to server!')