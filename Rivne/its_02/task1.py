# h = [j for i in d for j in i]

# e = [0]*10
# print(e)
#
# m = n = 5
# r = [[0 for i in range(m)] for j in range(n)]
# print(r)

# ---------------------- tuple ---------------------
# a = 5
# b = 6
# b, a = a, b
# print(a, b)
#
# c = a, b
# print(c)
# d = (1, 2, 55, 2)
# print(d)
#
# x, y, *z = 1, 2, 3, 4, 5
# print(x, y, tuple(z))
#
# print(tuple('text'))
# print(tuple([1]))
#
# print(len(d), max(d), min(d))
# print(d.index(2))
# print(d.count(2))
# d = d + tuple([77])
# print(d)

# ---------------------- dict ---------------------
d = {}
print(d)

d = dict(a1=1000, a2=2000, a3=3000)
print(d)
print(d['a1'])

d = dict({'k1': 111, 'k2': 222})
print(d)
print(d['k1'])

d = {'k1': 111, 'k2': 222}
print(d)
print(d['k2'])

a = {2: 'a', 'x': 'b', (1,): 'c'}
print(a)
print(a[2])

print(2 in a)
print(len(a))
print(list(a.keys()))
del a[2]
print(a)

for key in a.keys():
    print(f"\t{key}: {a[key]}")

a.update({'Some key': 2222})
print(a)

print(a.pop('x'))

print(a.values())

l1 = ['x', 'y']
l2 = [11111, 22222]
l3 = list(zip(l1, l2))
print(l3)
l3 = dict(zip(l1, l2))
print(l3)

l3 = {m: n for (m, n) in zip(l1, l2)}
print(l3)