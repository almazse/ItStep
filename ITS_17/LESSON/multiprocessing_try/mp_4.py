import multiprocessing as mp
import os


result = []


def square_list(my_list):
    global result
    for num in my_list:
        result.append(num ** 2)
    print(f'Result in process {os.getpid()}: {result}')


if __name__ == '__main__':
    the_list = [1, 3, 5, 7]
    p = mp.Process(target=square_list,
                   args=(the_list,))
    p.start()
    p.join()
    print(f'Result in main program: {result}')