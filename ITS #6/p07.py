import tkinter as tk
from p06 import f

W, H = 1200, 400
FONT = ('Courier', 10)
root = tk.Tk()
left, right = 0.0, 2.0
steps = 0

canvas = tk.Canvas(root, width=W, height=H, bg='#000')
canvas.pack(padx=20, pady=20)
canvas.create_line(0, H//2, W, H//2, fill='white', width=15)
canvas.create_line(0, H//2-10, 0, H//2+10, fill='white', width=15)
canvas.create_line(W, H//2-10, W, H//2+10, fill='white', width=15)
canvas.create_text(0, H//2-10, text='0.0',
                   fill='white', anchor='sw', font=FONT)
canvas.create_text(W, H//2-10, text='2.0',
                   fill='white', anchor='se', font=FONT)


def next_step():
    global left, right, steps
    center = (left + right) / 2
    x = center / 2.0 * W
    canvas.create_line(x, H // 2 - 10, x, H // 2 + 10,
                       fill='white', width=2)
    canvas.create_text(x, H // 2 - 10 - steps * 12, text=str(center),
                       fill='white', anchor='s', font=FONT)
    if f(left) * f(center) > 0:
        left = center
    else:
        right = center
    steps = steps + 1


btn1 = tk.Button(root, text='NEXT', command=next_step)
btn1.pack()


root.mainloop()
