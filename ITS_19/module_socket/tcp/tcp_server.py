import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8354))
s.listen()

print("Server started!")

while True:
    try:
        client, addr = s.accept()
    except KeyboardInterrupt:
        break
    else:
        result = client.recv(1024)
        print(f'message from {addr}: {result.decode("utf-8")}')
