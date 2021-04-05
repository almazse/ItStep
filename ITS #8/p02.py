a = [2, 3, 5, 7, 11, 13, 13, 19]

# удаление элементов
x = a.pop()
print(a, x)
print(len(a))

del a[2]
print(a)
print(len(a))

a.remove(13)
print(a)
print(len(a))

# добавление элементов
# a = a + [23, 29]
a.extend([23, 29])
print(a)
print(len(a))

a.append(23)
print(a)
print(len(a))