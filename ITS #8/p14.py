a = [1, 2, 3, 2, 3, 2, 2, 2, 2]

for n in 1, 2, 3, 4:
    if n in a:
        print(f"{n} содержится в {a}")
        ind = a.index(n)
        print(f"{n} на позиции {ind}")
    else:
        print(f"{n} не содержится в {a}")

for n in 1, 2, 3, 4:
    count = a.count(n)
    print(f"{n} содержится {count} раз")

# a.find(2) # AttributeError
