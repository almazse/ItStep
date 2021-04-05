# метод половинного деления
# корень из 2
LEFT, RIGHT = 0.0, 2.0
E = 0.000001


def f(x):
    return  x ** 2 - 2.0


if __name__ == '__main__':
    left, right = LEFT, RIGHT
    while (right - left) > E:
        center = (left + right) / 2
        print(left, right)
        if f(left) * f(center) > 0:
            left = center
        else:
            right = center
    print(center ** 2)
