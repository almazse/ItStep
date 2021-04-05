
# степень 2


def power_of_2_for(n):
    p = 1
    for _ in range(n):
        p = p * 2
    return p


def power_of_2_while(n):
    p = 1
    while n > 0:
        p = p * 2
        n = n - 1
    return p


if __name__ == '__main__':
    for n in 0, 3, 10:
        print(f"2 ** {n} = {power_of_2_for(n)}")
        print(f"2 ** {n} = {power_of_2_while(n)}")
