# a = [20, 30, 40, 50]

# a = []
# for e in range(20, 51, 10):
#     a.append(e)
#
# print(a)

a = list(range(20, 51, 10))
print(a)

b = [1, 2, 3]

c1 = a + b
print(c1)

c2 = b + a
print(c2)

# c3 = b + b + b + b
c3 = b * 4
print(c3)

c4 = [0] * 100
print(c4)
print(len(c4))