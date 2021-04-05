names = "Bobby Mary William Ann".split()

# lens = [len(name) for name in names]
# print(lens)


def get_len(s):
    return len(s)


# names.sort(key=get_len)
# print(names)

for name in sorted(names, key=get_len, reverse=True):
    print(name)
print()


def f(s):
    return s[-1]


for name in sorted(names, key=f):
    print(name)
