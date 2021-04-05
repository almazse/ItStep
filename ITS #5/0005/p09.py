import turtle as t

t.color("green")
t.width(2)
t.speed(5)


def draw_square():
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


def draw_polygon(n, a, fill=False):
    if fill:
        t.begin_fill()
    for _ in range(n):
        t.forward(a)
        t.left(360 / n)
    if fill:
        t.end_fill()


def draw_spiral(n, d):
    while n != 0:
        t.forward(n)
        t.left(360 / d)
        n -= 10

if __name__ == '__main__':
    draw_spiral(200, 3)
    t.exitonclick()

