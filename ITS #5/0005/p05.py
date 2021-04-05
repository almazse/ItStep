
start = 16

if __name__ == '__main__':
    x = start
    i = 1
    while x > 1:
        print(i, x)
        if x == 2.0:
            print("опа, двоечка")
            break
        x = x / 2
        i += 1
    else:
        print("while завершил работу")


