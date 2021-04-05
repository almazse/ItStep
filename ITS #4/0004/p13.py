from math import sqrt


def get_solution_quad_eq(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / 2 / a
        return f"x\u2081={x1:.3f}\nx\u2082={x2:.3f}"
    elif D == 0:
        x1 = -b / (2 * a)
        return f"x\u2081={x1:.3f}"
    else:
        return "no roots"


if __name__ == '__main__':
    a, b, c = 2, 13, 4
    print(get_solution_quad_eq(a, b, c))
