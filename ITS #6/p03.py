# найти НОД двух чисел
# 10, 15 -> 5


def get_NOD(a, b):
    min_val = min(a, b)
    d = min_val
    while True:
        if a % d == 0 and b % d == 0:
            return d
        d = d - 1


def get_NOD_euklid(a, b):
    big, small = max(a, b), min(a, b)
    while True:
        d = big % small
        if d == 0:
            return small
        else:
            big, small = small, d


if __name__ == '__main__':
    a, b = 60, 72
    print(f'НОД({a},{b}) = {get_NOD(a, b)}')
    print(f'НОД({a},{b}) = {get_NOD_euklid(a, b)}')
