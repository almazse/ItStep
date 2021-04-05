

def get_sum(a: float, b: float) -> float:
    return a + b


if __name__ == '__main__':
    a, b = 5, 10
    print(get_sum(a, b))
    a, b = '5', '10'
    print(get_sum(a, b))
