# ГЛОБАЛЬНАЯ ОБЛАСТЬ ВИДИМОСТИ


def foo():
    global var
    var = var + 500
    print(f"from foo: var = {var}")


if __name__ == '__main__':
    var = 2000
    print(f"from main: var = {var}")
    foo()
    print(f"from main: var = {var}")
