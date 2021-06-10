# my_list = [1, 3, 2, 5, 7, 8, 8, 9]
#
# s = set(my_list)
#
# a = set((1, 2, 5, 100))
#
# print(s, a)
#
# a = set.union(s, a)
# a.add(77)
# print(a)
# print(len(a))
#
# a.update([10, 20, 30, 7])
# print(a)
#
# a.discard(100000)
# print(a)
#
# a.remove(10000)
# print(a)
#
#
# c = frozenset(a)
# print(c)


# -------------- string ------------

# s = '  Some text  '.strip(' ')\
# # .capitalize().lower().upper().title().swapcase().center(20)
# s = s.replace('e', 'd')
# print(s.find('t'))
# print(s.rfind('D'))
# print(s.index('D'))
#
#
# a = list(s)
# print(''.join(a))

# -------------- function ------------

# def func(x: int, y = 0):
#     """
#     Description
#     """
#     return x + 5 + y
#
#
# print(func(3, 10))


# def myFunc(*args, **kwargs):
#     print(args, kwargs)
#     a = list(args)
#     print(enumerate(a))
#     for index, item in enumerate(a):
#         print(f'{index} -- {item}')
#
#
# myFunc(2, 3, 2, 5, 8, 7, 5, 4, key=2)

# def summa(*args):
#     return sum(args)/len(args)
#
#
# print(f'{summa(1, 5, 4, 7, 8, 9):f}')

# a = lambda x, y: x + y
#
# print(a(2, 3))
#
# x = 0
# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# a = gen()
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

from lib.module import summa as su
print(__name__)
# print(f'{su(1, 5, 4, 7, 8, 9):f}')
