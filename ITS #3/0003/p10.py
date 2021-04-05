from math import sqrt


def get_rectangle_area(a, b):
    # площадь прямоугольника
    return a * b


def hipotenuse(a, b):
    # гипотенуза прямоугольника
    return sqrt(a ** 2 + b ** 2)

if __name__ == '__main__':
    a1, b1 = 10.5, 25.2
    s1 = get_rectangle_area(a1, b1)
    print(f"S({a1}x{b1}) = {s1:.3f}")

    c1 = hipotenuse(a1, b1)
    print(c1)

