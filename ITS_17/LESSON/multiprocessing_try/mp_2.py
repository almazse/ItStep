from time import time
import multiprocessing as mp
import threading as th
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
    n = 3
    t1 = th.Thread(target=writer, args=('th.txt', 10**n))
    t1.start()
    t1.join()

    p1 = mp.Process(target=writer, args=('mp.txt', 10**n))
    p1.start()
    p1.join()
    print('THE END')