import socket

message = "Hello World!"

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.connect(('localhost', 8354))
s2.connect(('localhost', 8354))

s1.send(message.encode('utf-8'))
s2.send(message.encode('utf-8'))

s1.close()
s2.close()
