names = "Вася Петюня Сережка Вениамин".split()
print(names)

lens = [len(e) for e in names]
print(lens)

# lens = list(map(len, names))
# print(lens)

firsts = [name[0] for name in names]
print(firsts)

reversed_names = [name[::-1] for name in names]
print(reversed_names)

# for name in names:
#     print(name)

[print(name) for name in names]

# n: 1 + 2 + 3 + 4 = 10

def show_sum(n):
    # arr = [str(e) for e in range(1, n+1)]
    arr = list(map(str, range(1, n+1)))
    print(" + ".join(arr) + " = " + str(sum(range(1, n+1))))

show_sum(8)