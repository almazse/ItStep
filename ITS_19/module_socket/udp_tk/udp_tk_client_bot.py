import socket
import json
import random
import time

colors = ['green', 'blue', 'red', 'tomato', 'black', 'orange']

for _ in range(100):
    time.sleep(1)
    data = {'x': random.randint(20, 780),
            'y': random.randint(20, 580),
            'r': random.randint(5, 20),
            'color': random.choice(colors)}

    message = json.dumps(data)

    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(message)
    s1.sendto(message.encode('utf-8'), ('localhost', 8354))


