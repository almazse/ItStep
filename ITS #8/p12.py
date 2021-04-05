# все ли эл-ты четные?

a = [2, 4, 12, 24, 120]

for e in a:
    if e % 2 != 0:
        print("NO")
        break
else:
    print("YES")

# хотябы один четный элемент?
b = [1, 7, 5, 99, 3]

for e in b:
    if e % 2 == 0:
        print("YES")
        break
else:
    print("NO")