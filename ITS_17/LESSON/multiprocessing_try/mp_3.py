from time import time
from multiprocessing import Process, cpu_count
import random


def writer(filename, rows):
    start_time = time()
    with open(filename, 'w') as file:
        for i in range(rows):
            r = random.Random()
            file.write(f'{i:0>9} {r}\n')
    end_time = time()
    print(f'{(end_time-start_time) * 1000:2.2f} ms')


if __name__ == '__main__':
    n = 5
    n_cpu_s = cpu_count()
    processes = [Process(target=writer,
                         args=(f'mp_{i}.txt', 10**n))
                         for i in range(n_cpu_s)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print('THE END')