# TUPLE - неизменияемый список

a = (2, 3, 5, 7, 11, 13, 17, 19)
b = list(a)
print(a.__sizeof__(), b.__sizeof__())
c = tuple(b)
print(c, type(c))

for i in range(len(c)):
    print(c[i])

for i, e in enumerate(c):
    print(i, e)

for e in c:
    print(e)

# c[0] = 1 # TypeError
# c.append(77) # AttributeError


def f(n):
    return n ** 2, n ** 3


res1, res2 = f(5)
print(res1)
print(res2)

res = f(3)
print(res)

e = [33]
print(e, type(e))

e = (33,)
print(e, type(e))
