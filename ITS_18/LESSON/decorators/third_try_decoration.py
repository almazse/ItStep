from functools import wraps


def repeat(n=5):
    def _repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper
    return _repeat


twice = repeat(2)


@twice
def greeter(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    greeter('Kirill')