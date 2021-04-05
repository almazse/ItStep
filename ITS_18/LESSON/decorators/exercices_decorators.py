def h1(func):
    def wrapper(value):
        value = f'<h1>{func(value)}</h1>'
        return value
    return wrapper


@h1
def hello_word(name):
    """
    result: "<h1>Oleg</h1>"
    :param name: str
    :return: str
    """
    return f'Hello, {name}'


if __name__ == '__main__':
    print(hello_word('Kirill'))