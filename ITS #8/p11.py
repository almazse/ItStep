def get_list(n):
    arr = []
    for i in range(n):
        arr.append(int(input(f"a[{i}] = ")))
    return arr


def gev_avg_list(arr):
    return sum(arr) / len(arr)


if __name__ == '__main__':
    a =  get_list(4)

    print(f"S = {sum(a)}")
    print(f"max el. = {max(a)}")
    print(f"min el. = {min(a)}")
    print(f"avg = {gev_avg_list(a)}")