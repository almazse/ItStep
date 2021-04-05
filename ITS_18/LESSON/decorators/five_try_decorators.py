from time import time


class DecorationTimeit:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        self.func(*args, **kwargs)
        end_time = time()
        print(f'Function {self.func} was working for: {end_time - start_time}')

@DecorationTimeit
def calculate_factorial(number):
    result = 1
    for n in range(1, number):
        result *= n
    print(result)


if __name__ == '__main__':
    calculate_factorial(55)