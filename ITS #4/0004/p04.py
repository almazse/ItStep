# ОБЛАСТЬ ВИДИМОСТИ


def foo():
    print(f"from foo: var = {var}")


if __name__ == '__main__':
    var = 2000
    foo()
    print(f"from main: var = {var}")
