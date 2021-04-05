# отрезаем квадраты от прямоугольника
a, b = 16, 10

big, small = max(a, b), min(a, b)

while big != small:
    print(f"Отрезаем квадрат {small}")
    big = big - small
    big, small = max(big, small), min(big, small)

print(f"стался квадрат {small}")
