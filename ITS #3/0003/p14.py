# S = 1 + 2 + 3 + ... + n


def get_sum_series(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


def get_factorial(n):
    # n!= 1 * 2 * ... * n
    p = 1
    for i in range(1, n+1):
        p = p * i
    return p


if __name__ == '__main__':
    n = 12
    s = get_sum_series(n)
    print(f"S(1...{n}) = {s}")

    # print((n + 1) * n // 2)

    print(f"{n}! = {get_factorial(n)}")
