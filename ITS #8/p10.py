# ввод эл-тов списка с клавиатуры

N = 5


def get_list(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"a[{i}] = ")))
    return arr


def get_sum_list(arr):
    s = 0
    for e in a:
        s = s + e
    return s


def get_max_list(arr):
    m = arr[0]
    for e in arr[1:]:
        if e > m:
            m = e
    return m


if __name__ == '__main__':
    a = get_list(N-1)
    print(a)
    s = get_sum_list(a)
    print(f"S = {s}")
    print(f"max element = {get_max_list(a)}")
