# проверка является ли целое число простым
# 2 3 5 7 11 13 17 19 23 ...


def is_prime_number(n):
    for d in range(2, n):
        if n % d == 0:
            return False
        if d > n ** 0.5:
            return True


def is_prime_number2(n):
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            return False
        d += 1
    return True


if __name__ == '__main__':
    for num in 5, 8, 19, 2147483647:
        if is_prime_number(num):
            print(f'{num} - простое')
        else:
            print(f'{num} - непростое')

        if is_prime_number2(num):
            print(f'{num} - простое')
        else:
            print(f'{num} - непростое')