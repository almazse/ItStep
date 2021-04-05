from p04_multidim_arrays import show_matrix


# def get_zeros(m, n):
#     temp = []
#     for row in range(m):
#         z = []
#         for col in range(n):
#             z.append(0)
#         temp.append(z)
#     return temp


def get_zeros(m, n):
    return [[0] * n] *m


if __name__ == '__main__':
    z1 = get_zeros(m=4, n=9)
    show_matrix(z1)