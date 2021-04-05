# случайные процессы

import random
# random.seed(100)

# случайное число на интервале 0...1000
for _ in range(3):
    x = random.random() * 1000
    print(x)

# случайное целое число от a до b включ.
a, b = 10, 20
for _ in range(3):
    n = random.randint(a, b)
    print(n)

# случайный элемент
colors = ['red', 'green', 'blue']
for _ in range(3):
    c = random.choice(colors)
    print(c)

# случ. подмножество
for _ in range(3):
    s = random.sample(colors, 2)
    print(s)
