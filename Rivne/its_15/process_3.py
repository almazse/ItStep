import time
import tracemalloc
from multiprocessing import Pool

def singe_function(x):
   return x ** x


def main():
    p = Pool()
    p = p.map(singe_function([i for i in range(100000, 10000016)]))

tracemalloc.start()
start = time.time()

main()

print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time()-start))