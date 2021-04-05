# LIST COMPREHENSION - генерация списков
from math import sqrt

# 1 4 9 16 25 36 49

# a = []
# for i in range(1, 8):
#     a.append(i ** 2)
#
# print(a)

a = [i ** 2 for i in range(1, 8)]
print(a)

# b = []
# for e in a:
#     b.append(int(sqrt(e)))
#
# print(b)

b = [int(sqrt(e)) for e in a]
print(b)

s = "abracadabra"

uppers = [e.upper() for e in s]
print(uppers)

c = [1, 2, 3, 4, 11, 13, 22, 19, 66, 55]
# c1 = []
# for e in c:
#     if e % 2 != 0:
#         c1.append(e)
# print(c1)

c1 = [e for e in c if e % 2 != 0]
print(c1)

# 1 9 25 49 81 121
d1 = [e ** 2 for e in range(1, 12, 2)]
print(d1)
d2 = [e ** 2 for e in  range(1,12) if e % 2 != 0]
print(d2)
