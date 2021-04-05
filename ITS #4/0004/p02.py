
def loop_breaker(n=8):
    for i in range(1, 6):
        for j in range(2, 7):
            print(f"i={i}, j={j}, i*j={i * j}")
            if i * j == n:
                print()
                return


# потестить счетчики
if __name__ == '__main__':
    loop_breaker()
    loop_breaker(n=6)
    loop_breaker(4)
