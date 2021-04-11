import socket

messages = 'Today is sunday! Perfect day to spend time with relatives'.split()

socket = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(len(messages))]

for s, message in zip(socket, messages):
    s.connect(('localhost', 8354))
    s.send(message.encode('utf-8'))
    s.close()
