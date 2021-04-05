# отрезаем квадраты от прямоугольника
import tkinter as tk

a, b = 10, 16
n = 1
big, small = max(a, b), min(a, b)
scale = 50
vertical = True
x, y = 0, 0

W, H = big * scale, small * scale

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()
while big != small:
    print(f"Отрезаем квадрат {small}")

    canvas.create_text(x + small * scale / 2, y + small * scale / 2,
                       text=str(small))

    if vertical:
        x = x + small * scale
        canvas.create_line(x, y, x, H)
    else:
        y = y + small * scale
        canvas.create_line(x, y, W, y)

    big = big - small
    if big < small:
        big, small = small, big
        vertical = not vertical

print(f"стался квадрат {small}")

canvas.create_text(x + small * scale / 2, y + small * scale / 2,
                       text=str(small))

root.mainloop()
