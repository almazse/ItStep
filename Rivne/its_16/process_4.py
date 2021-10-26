from data_dict import data
import time
import tracemalloc
from multiprocessing import Pool


def single_function(DATA):
    with open('test_4.txt', 'a') as f:
        for i in range(DATA[1]*100):
            f.write(DATA[0])


def pool_handler():
    p = Pool()
    p.map(single_function, data)


if __name__ == '__main__':

    tracemalloc.start()
    start = time.time()
    for item in data:
        pool_handler()

    print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
    print("ALL done {}".format(time.time()-start))