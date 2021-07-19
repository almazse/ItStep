import math


# ax^2-bx+c=0

def square(a_, b_, c_):
    d = b_ ** 2 - 4 * a_ * c_
    root_1 = (-b_+math.sqrt(d))/(2*a_)
    root_2 = (-b_-math.sqrt(d))/(2*a_)
    return root_1, root_2


if __name__ == '__main__':
    x1, x2 = square(1, -7, 10)
    print(x1, x2)
    # 5, 2

    x1, x2 = square(1, 7, 10)
    print(x1, x2)
    # -2, -5
