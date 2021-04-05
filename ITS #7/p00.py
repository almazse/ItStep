# ARKANOID

import tkinter as tk

WIDTH, HEIGHT = 500, 600
TIMEOUT = 50
x, y = 100, 300
vx, vy = -10, -10
R_BALL, C_BALL = 10, "yellow"
BG_CANVAS = "black"
# Параметры доски
x_pad = WIDTH / 2
W_PAD, H_PAD, C_PAD = 200, 50, "green"

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_CANVAS)
canvas.pack(padx=20, pady=20)

ball = canvas.create_oval(x - R_BALL, y - R_BALL, x + R_BALL,
                          y + R_BALL, fill=C_BALL)

pad = canvas.create_rectangle(x_pad - W_PAD // 2, HEIGHT - H_PAD,
                              x_pad + W_PAD // 2, HEIGHT, fill=C_PAD)

score = canvas.create_text(WIDTH, 0, text="000", fill="white", anchor="ne",
                           font=("Arial", 20))

points = 0

def game(e=None):
    global x, y, vx, vy, points
    x, y = x + vx, y + vy
    canvas.coords(ball, x - R_BALL, y - R_BALL, x + R_BALL, y + R_BALL)
    # print(f'Game! {x=}, {y=}')
    if x <= R_BALL or x >= WIDTH - R_BALL:
        vx = -vx
    if y <= R_BALL:
        vy = -vy
        points += 1
        canvas.itemconfig(score, text=f"{points:0>3}")

    # Отбив
    if x_pad - W_PAD // 2 <= x <= x_pad + W_PAD // 2 \
        and y == HEIGHT - H_PAD - R_BALL:
        vy = -vy
    if y < HEIGHT - R_BALL:
        root.update()
        root.after(TIMEOUT, game)
    else:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="GAME OVER",
                           fill="red", font=('Arial', 40))


def keypress(e):
    global x_pad
    code = e.keycode
    # print(code)
    if code == 27:
        root.destroy()
    if code == 37:
        x_pad = x_pad - 50
        canvas.coords(pad, x_pad - W_PAD // 2, HEIGHT - H_PAD,
                      x_pad + W_PAD // 2, HEIGHT)
    if code == 39:
        x_pad = x_pad + 50
        canvas.coords(pad, x_pad - W_PAD // 2, HEIGHT - H_PAD,
                      x_pad + W_PAD // 2, HEIGHT)


def mousemove(e):
    global x_pad
    x_pad = e.x
    canvas.coords(pad, x_pad - W_PAD // 2, HEIGHT - H_PAD,
                  x_pad + W_PAD // 2, HEIGHT)


canvas.bind('<Motion>', mousemove)
root.bind('<Key>', keypress)
canvas.bind('<Button-1>', game)
root.mainloop()
