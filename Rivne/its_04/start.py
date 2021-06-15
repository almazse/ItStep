import math
from time import sleep

#----------------------------------- Polimorfizm

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'My name is {self.name}. I am {self.age}.')
#
#     def voice(self):
#         print('Woof')
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'My name is {self.name}. I am {self.age}.')
#
#     def voice(self):
#         print('meow')
#
#
# cat1 = Cat('Kitty', 2)
# dog1 = Dog('Bob', 4)
#
# cat1.voice()
# cat1.info()
#
# dog1.voice()
# dog1.info()

#----------------------------------- Inheritance

# class A:
#
#     def m_1(self):
#         return '(From A m_1)'
#
#     def m_2(self):
#         return '(From A m_2)'
#
#
# class B:
#
#     def m_3(self):
#         return '(From B m_3)'
#
#     def m_2(self):
#         return '(From B m_2)'
#
#
# class C(B, A):
#     pass
#
#
# c = C()
#
# print(c.m_1(), c.m_2(), c.m_3())


# class Door:
#
#     colour = 'black'
#     material = 'wood'
#
#     def __init__(self, number, status='close'):
#         self.number = number
#         self.status = status
#
#     def open(self):
#         self.status = 'open'
#
#     def close(self):
#         self.status = 'close'
#
#
# class SecuredDoor(Door):
#
#     material = 'iron'
#
#     def __init__(self, number, status, locked=True):
#         #  super().__init__(number, status)
#         Door.__init__(self, number, status)
#         self.locked = locked
#
#     def open(self, key: bool):
#         self.locked = not key
#         if not self.locked:
#             self.status = 'open'
#
#
# door1 = Door(1, 'close')
#
# door1.open()
# print('door1', door1.status)
# print(door1.colour)
# # print(Door.colour)
#
# door2 = SecuredDoor(2, 'close')
# door2.open(False)
# print('door2', door2.status)
# print(door2.colour)
#
# print(door1.__dict__)
# print(door2.__dict__)
# print()
# print(door1.__dir__())
# print()
# print(door2.__dir__())
# print(door2)
#
#
# class Shape:
#     color = 'red'
#
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass
#
#     @staticmethod
#     def desc():
#         return 'Unknown figure!'
#
#     def __str__(self) -> str:
#         return 'Instance of ' + self.name
#
#     def __repr__(self) -> str:
#         return 'Figure: ' + self.name
#
#     def __del__(self):
#         print('Figure: ' + self.name + ' was remowed!')
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius
#
#     @classmethod
#     def fig(cls, color: str):
#         cls.color = color
#         return 'ClassMethod: ' + color
#
#     @staticmethod
#     def func(x):
#         return 'Static method! ' * x
#
#     def desc(self):
#         return 'This is a ' + self.name
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#
# circle = Circle(10)
# print(circle.area())
# print(circle.__repr__())
#
# print(circle.__class__)
# print(Circle.__class__)
#
# print(type(circle) == '__main__.Circle')
# print(Circle.__mro__)
# print(circle.__module__)
# print(isinstance(circle, Circle))
# print(isinstance(circle, Shape))
#
# # sleep(5)
#
# print(circle.func(5))
# print(circle.fig('yellow'))


# class Singleton:
#     obj = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.obj is None:
#             cls.obj = object.__new__(cls, *args, **kwargs)
#         return cls.obj
#
#     def __init__(self):
#         print('INIT ', type(self))
#
#
# s1 = Singleton()
# s2 = Singleton()
#
# print(id(s1))
# print(id(s2))

class MyCl:
    cm = []
    ci = 'cl_inm'

    def __init__(self):
        self.im = []
        self.ii = 'inst_inm'


a = MyCl()
print(a.cm, a.ci, a.im, a.ii)

b = MyCl()
b.cm.append(11)
b.ci = 'new cl_inm'
b.im.append(22)
b.ii = 'new_ii'
print(a.cm, a.ci, a.im, a.ii)
print(b.cm, b.ci, b.im, b.ii)

c = MyCl()
c.cm.append(33)
c.ii = 'C_new_ii'

print(c.cm, c.ci, c.im, c.ii)
