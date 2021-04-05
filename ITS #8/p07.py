# a = [100, 200, 300, 400]

a = list(range(100, 401, 100))
print(a)

b = a.copy() # new list
print(b)

a[1] = 222
b[0] = 777
print(b)
print(a)
