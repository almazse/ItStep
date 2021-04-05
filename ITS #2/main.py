# a = 1
# b = 2
# print(f"{a = }, {b = }")
# temp = a
# a = b
# b = temp
# print(f"a = {a}, b = {b}")

# a, b = 1, 2
# print(f"a = {a}, b = {b}")
# b, a = a, b
# print(f"a = {a}, b = {b}")

# BOOL True / False

# a, b = False, False
# a_and_b = a and b
# a_or_b = a or b
# not_a, not_b = not a, not b
# a_xor_b = a != b
# print(f"{a=} {b=} {a_and_b=} {a_or_b=} {not_a=} {not_b=} {a_xor_b=}")

# a, b = False, True
# a_and_b = a and b
# a_or_b = a or b
# not_a, not_b = not a, not b
# a_xor_b = a != b
# print(f"{a=} {b=} {a_and_b=} {a_or_b=} {not_a=} {not_b=} {a_xor_b=}")

# a, b = True, False
# a_and_b = a and b
# a_or_b = a or b
# not_a, not_b = not a, not b
# a_xor_b = a != b
# print(f"{a=} {b=} {a_and_b=} {a_or_b=} {not_a=} {not_b=} {a_xor_b=}")

# a, b = True, True
# a_and_b = a and b
# a_or_b = a or b
# not_a, not_b = not a, not b
# a_xor_b = a != b
# print(f"{a=} {b=} {a_and_b=} {a_or_b=} {not_a=} {not_b=} {a_xor_b=}")


# s = "77"
# n= int(s)
# print(n, type(n))


# n0, n1, n2, n3  = -1, 0, 1, 100
# print(n0, n1, n2, n3)
# b0, b1, b2, b3 = bool(n0), bool(n1), bool(n2), bool(n3)
# print(b0, b1, b2, b3)
# n0, n1, n2, n3 = int(b0), int(b1), int(b2), int(b3)
# print(n0, n1, n2, n3)

# s1, s2, s3 = "True", "False", ""
# b1, b2, b3 = bool(s1), bool(s2), bool(s3)
# print(b1, b2, b3)
# s1, s2, s3 = str(b1), str(b2), str(b3)
# print(s1, s2, s3)

#  ==  !=  >  <  >=  <=  in

# print("a" in "abcd")
# print("v" in "abcd")

# print(7 == 7)

# b = 8 == 8
# print(b)

# c = "xxx" != "xxx"
# print(c)

# print(10 > 4 and 7.5 == 7.5 and 99 < 99)

# print("u" in "xyz" or not 300 != 200)

# n = int(input("n = "))

# if n > 4:
#     print(f"{n} больше четырех")
#     print(":)")
# else:
#     print(f"{n} не больше четырех")
#     print(":(")

# a, b = input("a, b = ").split(",")
# a, b = int(a), int(b)

# if a < b:
#     print("a < b")
#     print(":)")
# else:
#     if a == b:
#         print("a equals b")
#         print(":(")
#     else:
#         print("a > b")
#         print("(^.^)")

# print("after \"IF\"")

# a, b = input("a, b = ").split(",")
# a, b = int(a), int(b)

# if a < b:
#     print("a < b")
#     print(":)")
# elif a == b:
#     print("a equals b")
#     print(":(")
# else:
#     print("a > b")
#     print("(^.^)")

# print("after \"IF\"")

# m = int(input("введите оценку в баллах: "))

# if m >= 90:
#     s = "A"
# elif m >= 85:
#     s = "B"
# elif m >= 75:
#     s = "C"
# elif m >= 70:
#     s = "D"
# elif m >= 60:
#     s = "E"        
# else:
#     s = "F"

# print(f"{m} означает \'{s}\'")


# print("ПРОВЕРКА ЧЕТНОСТИ")
# a, b = input("a, b = ").split(",")
# a, b = int(a), int(b)

# if a % 2 == 0 and b % 2 == 0:
#     print("оба четные")

# elif a % 2 == 0 or b % 2 == 0:
#     print("одно четное, одно нечетное")

# else:
# print("оба четные")

# x, y = input("Введите x,y: ").split(",")
# x, y = float(x), float(y)

# if x > 0 and y > 0:
#     print(to_roman(1),"четверть")
# elif x < 0 and y > 0:
#     print("2-ая четверть")
# elif x < 0 and y < 0:
#     print("3-ая четверть")
# elif x > 0 and y < 0:
#     print("4-ая четверть")    


# consumption = 8.5
# fuel = 12.0

# distance = float(input("Введите расстояние: "))

# fuel_per_km = consumption / 100
# distance_can_go = fuel / consumption * 100

# if distance > distance_can_go:
#     d = distance - distance_can_go
#     print(f"не доеду {d:.1f} км")
# else:
#     f = fuel - distance / 100 * consumption
#     print(f"доеду, и останется {f:.1f} л топлива")

# from math import sqrt

# x, y = input("Введите x,y: ").split(",")
# x, y = float(x), float(y)

# r = 2

# if sqrt(x ** 2 + y ** 2) > r ** 2:
#     print(f"точка ({x}, {y}) вне окружности R={r}")
# else:
#     print(f"точка ({x}, {y}) внутри окружности R={r}")

# тернарный (троичный) оператор

# x = -10
# y = 1 if x > 0 else 0
# print(f"{x = } {y = }")

# a, b = 10, 101

# print("a равно b") if a == b else print("a не равно b")
# print("a равно b" if a == b else "a не равно b")


# h1, v1 = input("координаты 1й клетки: ").split()
# h1, v1 = int(h1), int(v1)
# h2, v2 = input("координаты 2й клетки: ").split()
# h2, v2 = int(h2), int(v2)

# condition = (h1 + v1) % 2 == (h2 + v2) % 2

# if condition:
#     print(f"клетки ({h1}, {v1}) и ({h2}, {v2}) одинакового цвета")
# else:
#     print(f"клетки ({h1}, {v1}) и ({h2}, {v2}) разного цвета")


# h1, v1 = input("координаты 1й клетки: ").split()
# h1, v1 = int(h1), int(v1)
# h2, v2 = input("координаты 2й клетки: ").split()
# h2, v2 = int(h2), int(v2)

# condition = (h1 == h2) != (v1 == v2)

# if condition:
#     print(f"ладья из ({h1}, {v1}) бьет фигуру в клетке ({h2}, {v2})")
# else:
#     print(f"ладья из ({h1}, {v1}) не бьет фигуру в клетке ({h2}, {v2})")

# print(abs(10-18)) для лошадки)))

h, m = input("на часах: ").split(":")
h, m = int(h), int(m)


if h == 23 and m == 59:
    h1, m1 = 0, 0
elif m == 59:
    h1, m1 = h+1, 0
else:
    h1, m1 = h, m+1

print(f"через минуту: {h1:0>2}:{m1:0>2}")

# попробовать тернарный