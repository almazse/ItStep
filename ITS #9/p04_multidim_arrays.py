
a = [
    [2, 3, 4],
    [2, 115, 7],
    [3, 8, 9],
    [2, 2, 5],
]


# def show_matrix(arr):
#     for row in arr:
#         for el in row:
#             print(f"{el:^7}", end="")
#         print()


def show_matrix(arr):
    for row in arr:
        print("".join([f"{el:^7}" for el in row]))


if __name__ == '__main__':
    show_matrix(a)