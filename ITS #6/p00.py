import tkinter as tk

W, H = 600, 500
STEP, STEP2 = 100, 50
root = tk.Tk()

canvas = tk.Canvas(root, width=W, height=H, bg='#000')
canvas.pack(padx=20, pady=20)


def optic_illusion_1():
    canvas.delete('all')
    for i in range(1, W // STEP):
        x = STEP * i
        canvas.create_line(x, 0, x, H, fill='grey', width=20)

    for i in range(1, H // STEP):
        y = STEP * i
        canvas.create_line(0, y, W, y, fill='grey', width=20)

    for i in range(1, W // STEP):
        for j in range(1, H // STEP):
            x = STEP * i
            y = STEP * j

            canvas.create_oval(x-15, y-15, x+15, y+15, fill='white')


def optic_illusion_2():
    canvas.delete('all')
    canvas.create_rectangle(0, 150, W, H-150, fill='white')
    canvas.create_line(0, 300, W, 300, width=10)
    canvas.create_line(0, H-300, W, H-300, width=10)

    for i in range(W // STEP2 + 1):
        x = i * STEP2
        canvas.create_line(x, 150, W-x, H-150, width=5)


btn1 = tk.Button(root, text='иллюзия 1', command=optic_illusion_1)
btn1.pack()

btn2 = tk.Button(root, text='иллюзия 2', command=optic_illusion_2)
btn2.pack()

root.mainloop()
