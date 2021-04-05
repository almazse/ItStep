# сумма цифр числа

# 1234 -> 1+2+3+4=10


def sum_digits(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


def max_digit(n):
    md = 0
    while n > 0:
        if n % 10 > md:
            md = n % 10
        n = n // 10
    return md


if __name__ == '__main__':
    for n in 1234, 10000001, 222:
        print(f"сумма цифр числа {n} : {sum_digits(n)}")
        print(f"самая большая цифра числа {n} : {max_digit(n)}")
