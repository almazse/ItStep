from data_dict import data
import time
import tracemalloc
import logging
from multiprocessing import Pool


def single_function(name, delay):
    logging.info(f'Task {name} started.')
    time.sleep(delay)
    logging.info(f'Task {name} finished')


def main():
    p = Pool()
    p.map(single_function, data)


# ----------------------------------------

format_log = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_log, level=logging.INFO,
                    datefmt="%H:%M:%S")

tracemalloc.start()
start = time.time()
sum = 0
# 165
for item in data:
    # single_function(item[0], item[1])
    sum += item[1]
print(sum)
print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time() - start))
