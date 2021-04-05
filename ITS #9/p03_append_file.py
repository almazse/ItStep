import random
import time

names = "Billy Bobby Sammy Willy Dilly Joe".split()

FILENAME = "append.txt"

with open(FILENAME, "a") as f:
    for _ in range(5):
        time.sleep(1.0)
        random_name = random.choice(names)
        f.write(f"{random_name} - {time.strftime('%H:%M:%S')} \n")
