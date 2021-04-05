from time import time


def timeit_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f'Function {func} was working for: {end_time-start_time}')
    return wrapper


def validate_numbers(func):
    def wrapper(value):
        if isinstance(value, int):
            return func(value)
        raise ValueError('Value is not valid number')
    return wrapper


@validate_numbers
@timeit_decorator
def calculate_factorial(number):
    result = 1
    for n in range(1, number):
        result *= n
    print(result)


if __name__ == '__main__':
    calculate_factorial(55)