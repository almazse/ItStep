import random

for _ in range(7):
    r = random.randint(1, 15)
    print(r)
    if r == 13:
        print("ой-ей-ей")
        break
else:
    print("вот все и закончилось")
