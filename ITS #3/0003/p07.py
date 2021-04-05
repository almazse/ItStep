# y = sign(x)

def signum(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def signum2(x):
    return 1 if x > 0 else 0 if x == 0 else -1

if __name__ == '__main__':
    x = 29
    print(f"sign({x}) = {signum2(x)}")

    x = 0
    print(f"sign({x}) = {signum2(x)}")

    x = -100
    print(f"sign({x}) = {signum2(x)}")

