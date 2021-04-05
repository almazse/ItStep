import multiprocessing as mp


def print_square(arg):
    print(f'Square: {arg**2}\n', end='')


def print_cube(arg):
    print(f'Cube: {arg**3}\n', end='')


if __name__ == '__main__':
    n = 10
    p1 = mp.Process(target=print_square, args=(n,))
    p2 = mp.Process(target=print_cube, args=(n,))
    p1.start()
    p2.start()
    p2.join()
    print('The end')