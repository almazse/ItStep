# время через n минут


def show_time(h=23, m=55, n=10):
    h1, m1 = h, m
    print(f"{h1:0>2}:{m1:0>2}")
    for _ in range(n):
        m1 += 1
        h1 += (m1 // 60)
        m1 %= 60
        h1 %= 24
        if h1 == 0 and m1 == 0:
            print("новый день")
        print(f"{h1:0>2}:{m1:0>2}")



if __name__ == '__main__':
    show_time(n=20)
