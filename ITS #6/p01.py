import tkinter as tk
import random

W, H = 600, 500
R = 30

root = tk.Tk()

canvas = tk.Canvas(root, width=W, height=H, bg='#fff')
canvas.pack(padx=20, pady=20)


def click(e):
    x, y = e.x, e.y
    canvas.create_oval(x-R, y-R, x+R, y+R)
    # print(f'{x=}, {y=}')


def right_click(e):
    x, y = e.x, e.y
    canvas.create_rectangle(x - R, y - R, x + R, y + R, fill='lightgrey')


def clear():
    canvas.delete('all')


def get_rnd_color():
    """
    Returns random color
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f'#{r:0>2x}{g:0>2x}{b:0>2x}'


def random_circles():
    for i in range(10):
        color = get_rnd_color()
        x, y = random.randint(0, W), random.randint(0, H)
        canvas.create_oval(x - R, y - R, x + R, y + R,
                           fill=color)


btn_clear = tk.Button(root, text='очистить', command=clear)
btn_clear.pack()

btn_rnd_circles = tk.Button(root, text='случайные круги',
                            command=random_circles)
btn_rnd_circles.pack()


canvas.bind('<Button-1>', click)
canvas.bind('<Button-3>', right_click)

root.mainloop()
