import socket

STOP_WORD = 'stop'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8300))

while True:
    try:
        result = s.recv(1024)
        if result.decode() == STOP_WORD:
            break
    except KeyboardInterrupt:
        break
    else:
        print(f'message from client: {result.decode("utf-8")}')

print('Server terminated')