import multiprocessing as mp
import os


def square_list(my_list, result, square_sum) -> None:
    for index, number in enumerate(my_list):
        result[index] = number ** 2
    square_sum.value = sum(result)
    print(f'Result in process {os.getpid()}: {result[:]}')


if __name__ == '__main__':
    the_list = [1, 3, 5, 7]
    result = mp.Array('i', 4)
    square_sum = mp.Value('i')
    p = mp.Process(target=square_list,
                   args=(the_list, result, square_sum))
    p.start()
    p.join()
    print(f'Result in main progtam: {result[:]}')
    print(f'S = {square_sum.value}')