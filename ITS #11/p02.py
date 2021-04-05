def show_student(name, *marks):
    print(name)
    for mark in marks:
        print(mark)


def sum_pow(pow, *args):
    return sum([el ** pow for el in args])

if __name__ == '__main__':
    show_student("Jonson", 68, 76, 100, 55)
    print()
    print(sum_pow(2, 1, 2, 3))
    print(sum_pow(3, 10, 20))
