import socket
import json

x = int(input('Please enter X:'))
y = int(input('Please enter Y:'))
r = int(input('Please enter R:'))
color = input('Please enter color:')

data = {'x': x,
        'y': y,
        'r': r,
        'color': color}

message = json.dumps(data)

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.sendto(message.encode('utf-8'), ('localhost', 8354))

result = s1.recv(1024)
if result.decode('utf-8') == message:
    print('delivery confirmed')
s1.close()
