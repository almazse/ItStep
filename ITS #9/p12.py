import random


def get_random_list(n=10, max_value=100):
    return [random.randint(1, max_value) for _ in range(n)]


def f1(num):
    # return num % 10
    return int(str(num)[-1])


def f2(num):
    return sum([int(c) for c in str(num)])


# def f2(num):
#     s = 0
#     while num > 0:
#         s += num % 10
#         num //= 10
#     return s


if __name__ == '__main__':
    a = get_random_list(max_value=999)
    print(a)

    for e in sorted(a, key=f2):
        print(e)
