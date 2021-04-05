from math import pi

# y = 2x + 3

# def get_y(x):
#     y = 2 * x + 3
#     return y

def get_y(x):
    return 2 * x + 3


def get_circle_area(r):
    return pi * r ** 2


if __name__ == '__main__':
    x = 2.34
    y = get_y(x)
    print(f"x = {x}, y = {y}")

    r = 12.2
    print(f"R = {r}, S = {get_circle_area(r):.3f}")

