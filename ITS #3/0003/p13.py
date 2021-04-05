
def main():
    for i in range(8): # 0, 1, 2, 3, 4, 5, 6, 7:
        print(f"i = {i}")
    print()

    for j in range(2,7): # 2, 3, 4, 5, 6:
        print(f"j = {j}")
    print()

    for k in range(10, 23, 3): # 10, 13, 16, 19, 22:
        print(f"k = {k}")
    print()

    for m in range(1000, 7001, 100):
        print(m, end=" ")
    print()

    for n in range(10, 0, -1):
        print(n, end="  ")
    print()

    for m in range(1700, 999, -100):
        print(m, end=" ")
    print()
    
if __name__ == '__main__':
    main()
