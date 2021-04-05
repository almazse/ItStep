# угадай число

import random

a, b = 1, 100
SECRET = random.randint(a, b)

if __name__ == '__main__':
    print(f"<<< УГАДАЙ ЧИСЛО ОТ {a} ДО {b}! >>>")
    counter, left, right = 0, a, b
    while True:
        counter += 1
        choice = int(input(f"{counter}) ваш вариант ({left} - {right}): "))
        if choice < SECRET:
            print("недолет")
            left = choice + 1
        if choice > SECRET:
            print("перелет")
            right = choice - 1
        if choice == SECRET:
            print("BINGO!")
            break
    print("<<< GAME OVER >>>")

