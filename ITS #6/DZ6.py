from  tkinter import *
import random

WIDTH, HEIGHT = 600, 500
FONT = ('Courier', 20)
RADIUS = 10

first_x, first_y, last_x, last_y, char_num = 0, 0, 0, 0, 65
finish = False

root = Tk()
root.title("СЕТКА")


def reset_program():
    # Сброс программы
    global finish, first_x, first_y, last_x, last_y, char_num
    finish = False
    first_x, first_y, last_x, last_y, char_num = 0, 0, 0, 0, 65
    canvas.delete('all')
    label.config(text="")


# Верхнее меню
main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label='Сброс', command=reset_program)

# полотно
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#fff')
canvas.pack(padx=20, pady=20)

label = Label(text="", font="Arial 10")
label.pack()


def get_rnd_color():
    # Returns random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f'#{r:0>2x}{g:0>2x}{b:0>2x}'


def left_click(e):
    if finish:
        return

    global first_x, first_y, last_x, last_y, char_num
    x, y = e.x, e.y
    label.config(text=f"{x=},{y=}")
    color = get_rnd_color()
    canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=color)

    canvas.create_text(x, y-RADIUS, text=chr(char_num), anchor='sw', font=FONT)
    char_num += 1

    if not first_x:
        first_x, last_x = x, x
        first_y, last_y = y, y

    canvas.create_line(last_x, last_y, x, y, fill='grey', width=2)

    last_x = x
    last_y = y


def right_click(e):
    global finish
    if finish:
        return
    canvas.create_line(last_x, last_y, first_x, first_y, fill='grey', width=2)
    finish = True


canvas.bind('<Button-1>', left_click)
root.bind('<Button-3>', right_click)
root.mainloop()
