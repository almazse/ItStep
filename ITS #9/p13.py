from p08_switch_rows_cols_el import get_square_matr, show_matrix
import random


def get_sum_row(row):
    return sum(row)


def foo(row):
    return row[-1] % 10


if __name__ == '__main__':
    s = get_square_matr(4)
    random.shuffle(s)
    show_matrix(s)

    for row in sorted(s, key=get_sum_row):
        print(row)

    print()

    for row in sorted(s, key=foo):
        print(row)
