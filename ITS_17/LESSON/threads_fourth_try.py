from threading import Thread, currentThread


def doubler(arg):
    res: int
    for _ in range(100500):
        for _ in range(100):
            res = 2 * arg
    name = currentThread().getName()
    print(f'result={res} from {name}\n', end='')


if __name__ == '__main__':
    names = ['Thread 1', 'Thread 2', 'Thread 3']
    values = [10, 13, 17]
    threads = [Thread(target=doubler,
                      args=(value,),
                      name=name) for name, value in zip(names, values)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print('END\n', end='')