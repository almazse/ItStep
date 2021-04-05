import random

if __name__ == '__main__':
    a = list(range(1, 8))
    random.shuffle(a)
    print(a)

    a.sort()
    print(a)

    a.sort(reverse=True)
    print(a)

    b = sorted(a)
    print(b)
    c = sorted(a, reverse=True)
    print(c)

    names = "Bobby Mary Billy Ann".split()
    # names.sort()
    # print(names)

    for i, name in enumerate(sorted(names), start=1):
        print(f"{i}) {name}")