import socket
import time

while True:
    try:
        time.sleep(0.5)
        message = 'ping'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = s.sendto(message.encode('utf-8'), ('127.0.0.1', 8300))
        print(f'{message} sent')
    except KeyboardInterrupt:
        break