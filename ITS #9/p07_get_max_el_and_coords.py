from p04_multidim_arrays import show_matrix

a = [
    [2, 3, 4],
    [2, 115, 7],
    [3, 8, 9],
    [2, 2, 5],
]


# def get_max_el(arr):
#     max_el = arr[0][0]
#     for row in arr:
#         for el in row:
#             if el > max_el:
#                 max_el = el
#     return max_el


def get_max_el(arr):
    return max(max(row) for row in arr)


def get_max_coords(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == get_max_el(arr):
                return row, col


if __name__ == '__main__':
    # m = a[1][1]
    # print(m, type(m))
    # a[1][1] = 100
    show_matrix(a)
    me = get_max_el(a)
    print(me)
    print(get_max_coords(a))