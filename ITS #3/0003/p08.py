
# def is_evan(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

def is_evan(num):
    return num % 2 == 0


if __name__ == '__main__':
    n = 11
    if is_evan(n):
        print(f"{n} - четное число")
    else:
        print(f"{n} - нечетное число")

    s = "" if is_evan(n) else "не"

    print(f"{n} - {s}четное число")