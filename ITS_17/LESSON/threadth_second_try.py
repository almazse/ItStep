from threading import Thread, currentThread
from time import sleep


def doubler(arg):
    res = 2 * arg
    sleep(0.5)
    name = currentThread().getName()
    print(f'result={res} from {name}\n', end='')


if __name__ == '__main__':
    names = ['Thread 1', 'Thread 2', 'Thread 3']
    vals = [10, 13, 17]
    for name, value in zip(names, vals):
        t = Thread(target=doubler,
                   args=(value,),
                   name=name)
        t.start()
    print('hello from', currentThread().getName())