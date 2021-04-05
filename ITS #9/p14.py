from tkinter import *
import random

CELL_SIZE= 100

captions = [str(i) for i in range(1, 16)] + [""]
target = [str(i) for i in range(1, 16)] + [""]
random.shuffle(captions)
print(captions)

root = Tk()
canvas = Canvas(root, width=4 * CELL_SIZE, height=4 * CELL_SIZE,
                bg="#000")
root.geometry(f'+{root.winfo_screenwidth() // 2 - 4 * CELL_SIZE // 2}+'
              f'{root.winfo_screenheight() // 2 - 4 * CELL_SIZE // 2}')

canvas.pack()


def draw():
    canvas.delete("all")
    for i in range(1, 4):
        canvas.create_line(0, i * CELL_SIZE, 4 * CELL_SIZE, i * CELL_SIZE,
                           fill="green", width=3)
        canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, 4 * CELL_SIZE,
                           fill="green", width=3)

    for i, caption in enumerate(captions):
        row, col = i // 4, i % 4
        canvas.create_text(col * CELL_SIZE + CELL_SIZE // 2,
                           row * CELL_SIZE + CELL_SIZE // 2,
                           text=str(caption), fill="green",
                           font=("Arial", 30))
    check()

def left():
    e_i = captions.index("")
    if e_i % 4 != 3:
        captions[e_i], captions[e_i + 1] = captions[e_i + 1], captions[e_i]


def right():
    e_i = captions.index("")
    if e_i % 4 != 0:
        captions[e_i], captions[e_i - 1] = captions[e_i - 1], captions[e_i]


def up():
    e_i = captions.index("")
    if e_i < 12:
        captions[e_i], captions[e_i + 4] = captions[e_i + 4], captions[e_i]


def down():
    e_i = captions.index("")
    if e_i > 3:
        captions[e_i], captions[e_i - 4] = captions[e_i - 4], captions[e_i]


def check():
    if all(captions[i] == target[i] for i in range(len(target))):
        canvas.create_text(4*CELL_SIZE / 2, 4*CELL_SIZE / 2,
                           text="ПОБЕДА!", font=("Arial", 30), fill="red")


def cheet():
    global captions
    captions = "1 2 3 4 5 6 7 8".split() + [""] + "10 11 12 9 13 14 15".split()



def keypress(event):
    c = event.keycode
    if c == 37:
        left()
    if c == 38:
        up()
    if c == 39:
        right()

    if c == 40:
        down()

    if c == 32:
        cheet()

    if c in (37, 38, 39, 40, 32):
        draw()


draw()
root.bind("<Key>", keypress)
root.mainloop()
