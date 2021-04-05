from functools import reduce
# s = ["111", "222", "777", "888", "999", "1000"]
s = "111 222 777 888 999 1000".split()

print(s)

# a = [int(e) for e in s if int(e) % 2 == 0]
a = [int(e) for e in s if e[-1] in "02468"]
print(a)
print(sum(a))


def is_even(x):
    return x % 2 == 0


a1 = list(filter(is_even, map(int, s)))
print(a1)


def f(a, b):
    return a + b


s = reduce(f, a1)
print(s)
