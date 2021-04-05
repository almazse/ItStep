from threading import Thread, currentThread
from time import sleep, time


def doubler(arg):
    for _ in range(100500):
        for _ in range(500):
            res = 2 * arg
    sleep(0.5)
    name = currentThread().getName()
    print(f'result={res} from {name}\n', end='')


if __name__ == '__main__':
    names = ['Thread 1', 'Thread 2', 'Thread 3']
    vals = [10, 13, 17]
    # 14.939557313919067
    start_time = time()
    for name, value in zip(names, vals):
        t = Thread(target=doubler,
                   args=(value,),
                   name=name)
        t.start()
        t.join()
    end_time = time()
    print(end_time-start_time)
    print('hello from', currentThread().getName())

    # 14.670555114746094
    start_time = time()
    for name, value in zip(names, vals):
        doubler(value)
    end_time = time()
    print(end_time-start_time)
    print('hello from', currentThread().getName())
