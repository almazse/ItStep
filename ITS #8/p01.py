# LISTS

a = [2, 3, 5, 7, 11, 13, 17, 19]

print(f"a = {a}")

n = len(a)

print(f"Длинна {a} равна {n}")

for i in range(n):
    print(f"a[{i}] = {a[i]}")

print("foreach")
for e in a:
    print(e, end=" ")
print()

print("enumerate")
for i, e in enumerate(a, start=101):
    print(i, e)
