# "Зеленский Владимир Александрович" ->
# "В.А.Зеленский"


def foo(s):
    last, first, patr = s.split()
    # return first[0] + "." + patr[0] + "." + last
    return f"{first[0]}.{patr[0]}.{last}"


if __name__ == '__main__':
    name = "Зеленский Владимир Александрович"
    print(foo(name))
    name = "Шариков Полиграф Полиграфович"
    print(foo(name))
