
def show_cube(n):
    summa = (n + 1) * n // 2

    syllables = ""

    j = 0
    for i in range(1, summa*2, 2):
        if j == summa-1:
            syllables = syllables + str(i)
        elif j >= summa-n:
            syllables = syllables + str(i) + " + "
        j += 1

    print(f"{n}**3 = {syllables} = {n**3}")

if __name__ == '__main__':
    show_cube(1)
    show_cube(2)
    show_cube(3)
    show_cube(4)
    show_cube(5)
