from data_dict import data
import time
import tracemalloc


def clear_file():
    with open('test_4.txt', 'w') as f:
            f.write('')

def single_function(text, count):
    with open('test_4.txt', 'a') as f:
        for i in range(count*100):
            f.write(text)

clear_file()
tracemalloc.start()
start = time.time()
# for item in data:
#     single_function(item[0], item[1])

print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time()-start))