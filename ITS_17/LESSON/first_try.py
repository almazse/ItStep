from threading import Thread, currentThread
from time import sleep, time

def complex_func(end_range=125):
    result = 1
    for n in range(1, end_range):
        result *= n

    print(f'hi from with {end_range}', currentThread().getName())


if __name__ == '__main__':
    t = Thread(target=complex_func, name='John')
    t.start()
    # sleep(1)
    complex_func(225)
    print('hello from', currentThread().getName())