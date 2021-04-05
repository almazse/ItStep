
def bubble_sorting(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                print(f"switch {a[j]}, {a[j+1]}")
                a[j], a[j + 1] = a[j+1], a[j]


if __name__ == '__main__':
    a = [4, 3, 2, 1]
    bubble_sorting(a)
    print(a)
