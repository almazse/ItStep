# n
# s = 1! +2! + 3! + ... + n!
# n! = 1 * 2 * 3 ... *n

import time


def get_sum_factorials_slow(n):
    s = 0
    for i in range(1, n + 1):
        p = 1
        for j in range(1, i + 1):
            p = p * j
            # print("slow")
        s = s + p
    return s


def get_sum_factorials_faster(n):
    s = 0
    p = 1
    for i in range(1, n + 1):
        p = p * i
        # print("fast")
        s = s + p
    return s


if __name__ == '__main__':
    n = 1000
    tic = time.time()
    s1 = get_sum_factorials_slow(n)
    toc = time.time()
    t1 = toc-tic
    print(f"s1 = {s1}\nt1 = {t1}")
    tic = time.time()
    s2 = get_sum_factorials_faster(n)
    toc = time.time()
    t2 = toc - tic
    print(f"s2 = {s2}\nt2 = {t2}")
    print(round(t1 /t2, 1))


