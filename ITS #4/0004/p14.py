
def sum_nubers(n=5):
    s = 0.0
    for _ in range(n):
        value = float(input("Введите слагаемое: "))
        if value == 0.02:
            break
        s += value
    print(f"S = {s}")


if __name__ == '__main__':
    sum_nubers()
