def get_descr_evan_or_not(num):
    return "четное число " if num % 2 == 0 else "нечетное число"


if __name__ == '__main__':
    n = 11

    print(f"{n} - {get_descr_evan_or_not(n)}")
    n = 10

    print(f"{n} - {get_descr_evan_or_not(n)}")
