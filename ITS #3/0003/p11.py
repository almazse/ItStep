# ax^2 + bx + c = 0
from math import sqrt


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve(a, b, c):
    print(f"{a}x\u00b2 + {b}x + {c} = 0")
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / 2 / a
        print (f"два корня: \nx\u2081={x1:.3f}\nx\u2082={x2:.3f}")
    elif D == 0:
        x1 = -b / (2 * a)
        print (f"один корень: \nx\u2081={x1:.3f}")
    else:
        print("нет корней")

if __name__ == '__main__':
    a, b, c = 2, 13, 4
    solve(a, b, c)

    a, b, c = 1, 2, 1
    solve(a, b, c)

    a, b, c = 2, 2, 2
    solve(a, b, c)

