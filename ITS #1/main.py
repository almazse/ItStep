# INPUT / OUTPUT
# ������ ������

# print("Hello, World!")
# print('Hello, World!')

# print("�� ������� ������� ����� 'print'")
# print('�� ������� ������� ����� "print"')


# print('�� ������� ������� ����� \'print\'')
# print("�� ������� ������� ����� \"print\"")

# print("���\n���")
# print("00000\n0   0\n00000")

# print("����", end=' + ')
# print("����", end=' = ')
# print("������")

# print("����", "����", "�����")
# print(1, 2, 3, 4)

# print("����", "����", "�����", sep=">-->")
# print(1, 2, 3, 4, sep=" + ")

# ��� = ��������

# name = "����"
# age = 21

# print("���: ", name)
# print("�������: ", age)

# print("���: ", name, ", �������: ", age)

# print("���: %s, �������: %d" % (name, age))
# print("���: {}, �������: {}".format(name,age))
# # f-������
# print(f"���: {name}, �������: {age}")

# name1 = input("������ ������� ���: ")
# print(f"������, ������� {name1}!")

# name2 = input("������ ������� ���: ")
# print(f"������, ������� {name2}!")

# print(f"{name1} � {name2} ���� � ����.")

# poetry = """����� � ���� � ������ ������,
# �� ���� ����� ���� ����������"""

# print(poetry)

"""
���� ������ Python

str - ������
int - ������������� (����� �����)
float - ����� � ��������� ������
bool - ���������� (True / False)
list - ������ (������)
tuple - ������
set - ���������
dict - ������� (������������� ������)
class 
"""
# ������������� ������������
# name, age = "����", 21

# print(name, type(name))
# print(age, type(age))

# input �� ��������� ������
# x = int(input("x = "))
# y = int(input("y = "))

# x, y = input("x, y: ").split()
# x, y = int(x), int(y)

# print(x + y)
# print(x - y)
# print(x * y)
# print(round(x / y, 3))
# print(x ** y) # ���������� � �������
# print(x // y) # ������������� �������
# print(x % y) # ������� �� �������

# z = float("1.02")
# print(z ** 2)

# z1 = int(z)
# print(z1)

# import math

# r = float(input("R = "))

# �� = math.pi

# areaOfCircle = �� * r ** 2
# print(f"S = {areaOfCircle:.3f} ��\u00b2")

# from math import exp, e

# x = 1.7

# y = exp(x)
# print(f"exp({x:.4f}) = {y:.4f}")

# y = e ** x
# print(f"exp({x:.4f}) = {y:.4f}")

# y = pow(e, x)
# print(f"exp({x:.4f}) = {y:.4f}")

# name, breed = "���� ����-���".split()
# print(f"���: {name:^10}, ������: {breed:>15}")

# name, breed = "�������� ������".split()
# print(f"���: {name:^10}, ������: {breed:>15}")

# name, breed = "�� �������-�������".split()
# print(f"���: {name:^10}, ������: {breed:>15}")

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