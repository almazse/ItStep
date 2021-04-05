x = [0, 1, 50, 1000]


def f(arg):
    return arg ** 0.5


y = {x_: f(x_) for x_ in x}
print(y)
print(type(y) == dict)
print(isinstance(y, dict))

for x_ in x:
    print(x_, y[x_])