# ЛОКАЛЬНАЯ ОБЛАСТЬ ВИДИМОСТИ


def foo():
    var = 1000
    print(f"from foo: var = {var}")


if __name__ == '__main__':
    foo()
    # print(var) # NameError: name 'var' is not defined
