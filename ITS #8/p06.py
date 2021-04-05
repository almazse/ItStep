# d = [2, 4, 6, 8]

d = list(range(2, 9, 2))
print(d)

for i in range(len(d)):
    d[i] //= 2
    print(d[i], end=" ")

print()

# READ_ONLY
for e in d:
    e *= 2
    print(e, end=" ")

print()
print(d)

for i, e in enumerate(d):
    e = e * 2
    d[i] = e

print(d)
