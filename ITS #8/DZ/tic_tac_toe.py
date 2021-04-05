from tkinter import *
from tkinter import messagebox as mb

WIDTH, HEIGHT = 300, 300
HEADER_S = 120
FONT = "Comic Sans MS"
RECTANGLE = 70
cell = [["", "", ""], ["", "", ""], ["", "", ""]]
game_over = False
COLOR = ["red", "blue"]
player = "X"
player_line = ""
counter = [0, 0]
progress_counter = 0


def restart_game(e):
    global cell, game_over, progress_counter
    game_over = False
    cell = [["", "", ""], ["", "", ""], ["", "", ""]]
    playground.delete("Players")
    progress_counter = 0


# конец игры, вывод результатов игры
def end_game():
    global game_over, counter
    if not game_over:
        if player == "X":
            counter[0] += 1
        else:
            counter[1] += 1
        mb.showinfo(title="WINNER", message=f"{player} WINNER!!!")
        game_over = True
        playground.itemconfig(display_counter, text=f"{counter[0]} / {counter[1]}")


# Проверка победы
def check_win():
    global progress_counter
    progress_counter += 1

    if progress_counter >= 5:
        for i in range(3):
            if cell[i][0] == player and cell[i][1] == player and cell[i][2] == player:
                end_game()

            if cell[0][i] == player and cell[1][i] == player and cell[2][i] == player:
                end_game()

        if cell[0][0] == player and cell[1][1] == player and cell[2][2] == player:
            end_game()

        if cell[0][2] == player and cell[1][1] == player and cell[2][0] == player:
            end_game()

        if progress_counter == 9 and not game_over:
            mb.showinfo(title="TIE", message=f"No winners, tie.")


# Обработка клика по ячейке
def click(e, rows, cols):
    global player, player_line

    if not game_over and cell[rows][cols] == '':
        fill = (COLOR[0] if player == "X" else COLOR[1])
        playground.create_text(cols * RECTANGLE + RECTANGLE // 2, rows * RECTANGLE + RECTANGLE // 2, text=player,
                               fill=fill, font=(FONT, 20, "bold"), tags="Players")
        cell[rows][cols] = player
        check_win()

        playground.delete(player_line)
        if player == "X":
            player = "O"
            player_line = playground.create_line(135, RECTANGLE * 3 + 75, 185, RECTANGLE * 3 + 75,
                                                 fill=COLOR[1], width=5)
        else:
            player = "X"
            player_line = playground.create_line(25, RECTANGLE * 3 + 75, 75, RECTANGLE * 3 + 75,
                                                 fill=COLOR[0], width=5)


root = Tk()
root.title("Крестики нолики")
# окно по центру экрана
root.geometry(f'+{root.winfo_screenwidth() // 2 - WIDTH // 2}+'
              f'{root.winfo_screenheight() // 2 - (HEIGHT + HEADER_S) // 2}')
root.resizable(False, False)  # запретить растягивать

playground = Canvas(width=RECTANGLE*3, height=RECTANGLE*3 + HEADER_S, highlightthickness=0)
playground.grid(row=0, column=0)

# Генерация игрового поля 3 на 3 клетки
for row in range(3):
    for col in range(3):
        playground.create_rectangle(col * RECTANGLE, row * RECTANGLE + RECTANGLE,
                                    col * RECTANGLE + RECTANGLE, row * RECTANGLE, tags=f"{row}_{col}", fill="white")
        playground.tag_bind(f"{row}_{col}", "<Button-1>", lambda e="", rows=row, cols=col: click(e, rows, cols))

# Вывод игровой статистики
playground.create_text(40, RECTANGLE * 3 + 10, text="X", anchor="nw", fill=COLOR[0], font=(FONT, 20, "bold"))
playground.create_text(30, RECTANGLE * 3 + 50, text="player 1", anchor="nw", fill=COLOR[0])

player_line = playground.create_line(25, RECTANGLE * 3 + 75, 75, RECTANGLE * 3 + 75, fill=COLOR[0], width=5)

playground.create_text(RECTANGLE * 3 / 2, RECTANGLE * 3 + 30, text="vs", anchor="center", font=(FONT, 18))

display_counter = playground.create_text(RECTANGLE * 3 / 2, RECTANGLE * 3 + 55,
                                         text="0 / 0", anchor="center", font=(FONT, 10))

playground.create_text(RECTANGLE * 3 - 60, RECTANGLE * 3 + 10, text="O", anchor="nw",
                       fill=COLOR[1], font=(FONT, 20, "bold"))
playground.create_text(RECTANGLE * 3 - 70, RECTANGLE * 3 + 50, text="player 2", anchor="nw", fill=COLOR[1])

# Кнопка перезапуска игры
playground.create_text(RECTANGLE * 3 / 2, RECTANGLE * 3 + 90, text="\u21BA", anchor="center", fill="green",
                       font=(FONT, 30, "bold"), tags="restart_button")
playground.tag_bind("restart_button", '<Button-1>', restart_game)

root.mainloop()
