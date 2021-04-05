def describe_number(n=0):
    if n > 0:
        print(f"{n} - положительное число")
    elif n == 0:
        print(f"ноль!!!")
    else:
        print(f"{n} - отрицательное число")


if __name__ == '__main__':
    # x = int(input("n = "))
    # describe_number(x)

    describe_number(int(input("n = ")))

    # describe_number()