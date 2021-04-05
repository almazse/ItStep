from math import sin,radians

print("Введите данные:")
a = input("a (сторона треугольника) = ")
b = input("b (сторона треугольника) = ")
y = input("\U0001D6FE (угол между сторонами\u00B0) = ")

a, b, y = float(a), float(b), float(y)

S = (a * b) / 2 * sin(radians(y))
print(f"Площадь треугольника S = {S}")