import multiprocessing as mp
import os


def square(arg):
    return arg * arg


if __name__ == '__main__':
    the_list = [1, 2, 3, 4, 5]

    p = mp.Pool()

    result = p.map(square, the_list)

    print(result)