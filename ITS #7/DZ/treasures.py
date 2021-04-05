from math import sqrt
from tkinter import *
from tkinter import messagebox as mb
import random

WIDTH, HEIGHT = 500, 500
HEADER_S = 50
FONT = "Comic Sans MS"
count_lives = 10
game_over = False
treasure_x = random.randint(0, WIDTH)
treasure_y = random.randint(HEADER_S, HEIGHT)
treasure_radius = 20

root = Tk()
root.title("Остров сокровищ")
# окно по центру экрана
root.geometry(f'+{root.winfo_screenwidth()//2-WIDTH//2}+{root.winfo_screenheight()//2-(HEIGHT+HEADER_S)//2}')
root.iconbitmap('icon.ico')  # конка приложения
root.config(cursor='none')  # скрыть курсор
root.resizable(False, False)  # запретить растягивать

# Игровое поле canvas
canvas = Canvas(width=WIDTH, height=HEIGHT + HEADER_S, highlightthickness=0)
canvas.grid(row=0, column=0)

# Карта
landscape = PhotoImage(file='landscape.png')
canvas.create_image(0, 0, image=landscape, anchor="nw", tag="map")

# Cтатус бар
status_bar = PhotoImage(file='status_bar.png.')
canvas.create_image(0, 0, image=status_bar, anchor="nw")

# Вывод количества попыток
canvas.create_text(95, 25, text=f"Попытки: ", font=(FONT, 20), fill="white")
lives = canvas.create_text(180, 25, text=f"{count_lives}", font=(FONT, 20), fill="white")

# Вывод расстояния попыток
canvas.create_text(WIDTH - 145, 25, text=f"Расстояние: ", font=(FONT, 20), fill="white")
distance = canvas.create_text(WIDTH - 45, 25, text="---", font=(FONT, 20), fill="white")

# Лопата вместо курсора
shovel_cursor = PhotoImage(file='shovel.png')
canvas.create_image(-50, 0, image=shovel_cursor, anchor="nw", tag="shovel")

mb.showinfo(title="Цель игры", message="Найдите сокровище на карте. Количество попыток ограничено.")


# Перемещение мышки
def mouse_move(e):
    canvas.delete("shovel")
    canvas.create_image(e.x+1, e.y+1, image=shovel_cursor, anchor="nw", tag="shovel")


# Рестарт игры
def restart_game(e):
    global count_lives, game_over, treasure_x, treasure_y
    canvas.delete("restart_button")
    canvas.delete("text")
    count_lives = 10
    game_over = False
    treasure_x = random.randint(0, WIDTH)
    treasure_y = random.randint(HEADER_S, HEIGHT)

    canvas.itemconfig(distance, text="---")
    canvas.itemconfig(lives, text=count_lives)


# Клик мышки
def mouse_click(e):
    global count_lives, game_over

    # если игра окончена или клик по статусбару, ничего не делать
    if e.y <= HEADER_S or game_over:
        return

    # Отнимаем попытку
    count_lives -= 1
    canvas.itemconfig(lives, text=f"{count_lives}")

    # Если попыток не осталось, игра окончена
    if not count_lives:
        game_over = True
        canvas.delete("mark")
        canvas.create_text(WIDTH / 2, HEIGHT / 2 - 30, text="ИГРА ОКОНЧЕНА",
                           fill="red", font=(FONT, 40), tags="text")
        canvas.create_text(WIDTH / 2, HEIGHT / 2 + 30, text="сыграть еще раз",
                           fill="blue", font=(FONT, 20), tags="restart_button")
        return

    # Расчет дистанции
    a = max(treasure_x, e.x) - min(treasure_x, e.x)
    b = max(treasure_y, e.y) - min(treasure_y, e.y)

    distance_calc = sqrt(a ** 2 + b ** 2)

    if distance_calc <= treasure_radius:
        # Победа
        game_over = True
        canvas.delete("mark")
        canvas.create_text(WIDTH / 2, HEIGHT / 2 - 30, text="ПОБЕДА",
                           fill="red", font=(FONT, 40), tags="text")
        canvas.create_text(WIDTH / 2, HEIGHT / 2 + 30, text="сыграть еще раз",
                           fill="blue", font=(FONT, 20), tags="restart_button")
    else:
        # Ставим отметку
        canvas.create_text(e.x, e.y, text="x", fill="red", font=(FONT, 20), tag="mark")

        # Обновляем дистанцию
        canvas.itemconfig(distance, text=f"{distance_calc - treasure_radius:.0f}")


canvas.bind('<Motion>', mouse_move)
canvas.tag_bind("map", '<Button-1>', mouse_click)
canvas.tag_bind("restart_button", '<Button-1>', restart_game)
root.mainloop()
