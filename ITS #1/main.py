# INPUT / OUTPUT
# вторая строка

# print("Hello, World!")
# print('Hello, World!')

# print("мы изучаем функцию принт 'print'")
# print('мы изучаем функцию принт "print"')


# print('мы изучаем функцию принт \'print\'')
# print("мы изучаем функцию принт \"print\"")

# print("раз\nдва")
# print("00000\n0   0\n00000")

# print("Вася", end=' + ')
# print("Петя", end=' = ')
# print("дружба")

# print("Маша", "Даша", "Света")
# print(1, 2, 3, 4)

# print("Маша", "Даша", "Света", sep=">-->")
# print(1, 2, 3, 4, sep=" + ")

# имя = значение

# name = "Витя"
# age = 21

# print("Имя: ", name)
# print("Возраст: ", age)

# print("Имя: ", name, ", возраст: ", age)

# print("имя: %s, возраст: %d" % (name, age))
# print("имя: {}, возраст: {}".format(name,age))
# # f-строки
# print(f"имя: {name}, возраст: {age}")

# name1 = input("Ведите мужское имя: ")
# print(f"Привет, дорогой {name1}!")

# name2 = input("Ведите женское имя: ")
# print(f"Привет, дорогой {name2}!")

# print(f"{name1} и {name2} идут в кафе.")

# poetry = """Когда я стал с годами старше,
# со мною стали суше секретарши"""

# print(poetry)

"""
типы данных Python

str - строки
int - целочисленный (целые числа)
float - числа с плавающей точкой
bool - логический (True / False)
list - список (массив)
tuple - кортеж
set - множество
dict - словарь (ассоциативный массив)
class 
"""
# множественное присваивание
# name, age = "Витя", 21

# print(name, type(name))
# print(age, type(age))

# input по умолчанию строка
# x = int(input("x = "))
# y = int(input("y = "))

# x, y = input("x, y: ").split()
# x, y = int(x), int(y)

# print(x + y)
# print(x - y)
# print(x * y)
# print(round(x / y, 3))
# print(x ** y) # возведение в степень
# print(x // y) # целочисленное деление
# print(x % y) # остаток от деления

# z = float("1.02")
# print(z ** 2)

# z1 = int(z)
# print(z1)

# import math

# r = float(input("R = "))

# пи = math.pi

# areaOfCircle = пи * r ** 2
# print(f"S = {areaOfCircle:.3f} см\u00b2")

# from math import exp, e

# x = 1.7

# y = exp(x)
# print(f"exp({x:.4f}) = {y:.4f}")

# y = e ** x
# print(f"exp({x:.4f}) = {y:.4f}")

# y = pow(e, x)
# print(f"exp({x:.4f}) = {y:.4f}")

# name, breed = "Мася мейн-кун".split()
# print(f"имя: {name:^10}, порода: {breed:>15}")

# name, breed = "Василиса свинкс".split()
# print(f"имя: {name:^10}, порода: {breed:>15}")

# name, breed = "Ян скоттиш-бриттиш".split()
# print(f"имя: {name:^10}, порода: {breed:>15}")

# hours, minutes = 1, 5
# print(f"CURRENT TIME {hours:0>2}:{minutes:0>2}")

# money = 10000.3

# print(f"{money:,.2f}")

m = 100
print(m)
m = m + 1
print(m)
m += 1
print(m)
m = m - 1
print(m)
m -= 1
print(m)
m *= 2
print(m)
m /= 2
print(m)
m **= 2
print(m)
m //= 2
print(m)
m %= 2
print(m)