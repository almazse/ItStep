class DecorationLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Function {self.func} started')
        self.func(*args, **kwargs)
        print(f'Function {self.func} ended')


@DecorationLogger
def greeter(name):
    print(f'Hi, {name}! New Greeter Message')


@DecorationLogger
def good_night(name):
    print(f'Good Night! {name}')


if __name__ == '__main__':
    greeter(name='Kirill')
    good_night(name='Kirill')