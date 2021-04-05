def get_hello():
    print("работает функция get_hello")
    return "HELLO"

if __name__ == '__main__':
    s = get_hello()
    print(f"у нас есть \"{s}\"")