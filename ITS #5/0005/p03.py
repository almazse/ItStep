import random

n3, n4, n5 = 0, 0, 0
n = 12

if __name__ == '__main__':
    for _ in range(n):
        mark = random.randint(3, 5)
        if mark == 3:
            n3 += 1
        elif mark == 4:
            n4 += 1
        else:
            n5 += 1
    print(f"n3 = {n3}, n4 = {n4}, n5 = {n5}")
    print("----------------------------")

    height = max(n3, n4, n5)

    # height = n3 if n3 > n4 and n3 > n5 else n4 if n4 > n5 else n5
    # print(height)

    # print("3  4  5")
    symbol = "#"
    # for i in range(height):
    #     s3 = symbol if i < n3 else " "
    #     s4 = symbol if i < n4 else " "
    #     s5 = symbol if i < n5 else " "
    #     print(f"{s3}  {s4}  {s5}")

    for i in range(height, 0, -1):
        s3 = symbol if i <= n3 else " "
        s4 = symbol if i <= n4 else " "
        s5 = symbol if i <= n5 else " "
        print(f"{s3}  {s4}  {s5}")

    print("3  4  5")
