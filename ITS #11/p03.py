# *[1, 2, 3] -> 1, 2, 3

a = [1, 2, 3]
print(a)
print(*a, sep=" + ")

b = [10, 20, 30, 40, 50]
first = b[0]
tale = b[1:]
print(first, tale)

first, *tale = b
print(first, tale)