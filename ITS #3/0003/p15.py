
def get_power(a, n):
    # возвращает а в степени n
    sum_a = a
    for i in range(1, n):
        sum_a = sum_a * a

    return sum_a



if __name__ == '__main__':
    a, n = 2, 10
    print(get_power(a, n)) # 1024

    a, n = 5, 4
    print(get_power(a, n))  # 625


