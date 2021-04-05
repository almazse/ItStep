from p04_multidim_arrays import show_matrix


# def get_square_matr(n):
#     matr = []
#     el = 1
#     for row in range(1, n+1):
#         z = []
#         for col in range(1, n+1):
#             z.append(el)
#             el += 1
#         matr.append(z)
#     return matr

def get_square_matr(n):
    return [list(range(i*n+1, (i+1)*n+1)) for i in range(n)]


def switch_cols(arr, n1, n2):
    for row in arr:
        row[n1], row[n2] = row[n2], row[n1]


def switch_rows(arr, n1, n2):
    arr[n1], arr[n2] = arr[n2], arr[n1]


def switch_rows_by_el(arr, n1, n2):
    for col in range(len(arr[0])):
        arr[n1][col], arr[n2][col] = arr[n2][col], arr[n1][col]


if __name__ == '__main__':
    s = get_square_matr(5)
    show_matrix(s)
    print()
    switch_cols(s, 0, 3)
    show_matrix(s)

    print()
    switch_rows(s, 0, 4)
    show_matrix(s)

    print()
    switch_rows_by_el(s, 0, 4)
    show_matrix(s)