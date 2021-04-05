def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Function {func} started')
        func(*args, **kwargs)
        print(f'Function {func} ended')
    return wrapper


@logger
def greeter(name):
    print(f'Hi, {name}! New Greeter Message')


@logger
def good_night(name):
    print(f'Good Night! {name}')


if __name__ == '__main__':
    greeter(name='Kirill')
    good_night(name='Kirill')
