"""
Comment
"""
# Comment
# print(1, 'text', .3, 2.3, True, sep='\t', end='...\n')
# print("Word")
# x = 5.0
# print(f'This {x}')
# print('Number {:.0f} type {}'.format(x, type(x)))
# print("""Text
# very long""")
#
# y = input('Enter data: ')
# print(y)

# print(f'Text \
# word {55}', 55555)
#
# print('Next' + 'Text')

# + - * /
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)

# x = 5
# y = x
# y = 5
#
# print(id(x), x)
# print(id(y), y)
# print(x is y)

# print(3**2)
# print(type(True))

# import random
#
# x = random.random()
# x = random.randint(1, 10)
# x = random.uniform(1, 10)
# y = [1, 2, 3]
# x = random.choice(y)
# print(x)

# x = 'text'.upper().replace("T", "O", 1).rjust(50)
#
# print(x, len(x), x[::2])

x = 0
while x < 5:
    if x % 2 != 0:
        continue
    print(x)
    x += 1
