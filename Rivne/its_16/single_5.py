from data_dict import data
import time
import tracemalloc


# def clear_file():
#     with open('test_4.txt', 'w') as f:
#             f.write('')

def single_function_write(index):
    with open(f'files/read/file_{index+1}_read.txt', 'w') as f:
        # info = f.read()
        f.write(f'Read text {index+1}')

    # with open(f'files/write/file_{index+1}_write.txt', 'w') as f:
    #     f.write(info)

# clear_file()
tracemalloc.start()
start = time.time()
for i in range(10000):
    single_function_write(i)

print("Current %d, Peak %d" %tracemalloc.get_traced_memory())
print("ALL done {}".format(time.time()-start))