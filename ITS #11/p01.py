def f1(a, b):
    return a + b


def f2(arr):
    return sum(arr)


def f3(*x):
    print(type(x))
    return sum(x)


if __name__ == '__main__':
    print(f1(10, 20))

    print(f1(b=20, a=10))

    print(f2([10, 20, 30]))
    print(f2((10, 20, 30)))

    print(f3(1, 2, 3))
    print(f3(1, 2, 3, 4, 5, 6))