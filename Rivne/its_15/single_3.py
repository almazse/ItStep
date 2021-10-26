import time
import tracemalloc


def singe_function(x):
   return x ** x

tracemalloc.start()
start = time.time()

for i in range(100000, 1000005):
    singe_function(i)

print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time()-start))