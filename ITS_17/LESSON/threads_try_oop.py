from threading import Thread, currentThread
from time import sleep


class Doubler(Thread):
    def __init__(self, arg, name):
        Thread.__init__(self)
        self.arg = arg
        self.name = name

    def run(self):
        """
        runs with start(
        :return: None
        """
        result = 2 * self.arg
        sleep(self.arg/4)
        print(f'result={result} from {self.name}\n', end='')


if __name__ == '__main__':
    names = ['Thread 1', 'Thread 2', 'Thread 3']
    values = [10, 13, 17]
    threads = [Doubler(value, name) for name, value in zip(names, values)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print('END\n', end='')