from tkinter import *

color1, color2 = "#B58762", "#EFDAB4"
size_cell = 60
size_cell_sign = 30
chess = []
chess_win = []

root = Tk()
root.config(bg=color2)
root.title("Шахматы")

canvas = Canvas(width=size_cell * 8 + size_cell_sign * 2, height=size_cell * 8 + size_cell_sign * 2,
                highlightthickness=0, bg=color2)
canvas.grid(row=0, column=0)

text = Text(root, width=20, height=5, bg=color2, fg=color1, highlightthickness=2, highlightbackground=color1,
            highlightcolor=color1, insertbackground=color1, relief="flat", state='disabled', font=("Arial", 15))
text.config(state='normal')
text.insert(1.0, "Нет комбинаций")
text.config(state='disabled')
text.grid(row=0, column=1, padx=(0, 30), pady=30, sticky="nswe")

# Генерация ячеек
for j in range(0, 8):
    for i in range(0, 8):
        if j % 2 == 0:
            fill = color2 if i % 2 == 0 else color1
        else:
            fill = color1 if i % 2 == 0 else color2

        canvas.create_rectangle(i * size_cell + size_cell_sign, j * size_cell + size_cell_sign,
                                i * size_cell + size_cell + size_cell_sign, j * size_cell + size_cell + size_cell_sign,
                                fill=fill, outline="", tags=f"{i}_{j}")
        canvas.tag_bind(f"{i}_{j}", "<Button-1>", lambda e="", row=i, col=j: click(e, row, col))

canvas.create_rectangle(size_cell_sign, size_cell_sign, size_cell * 8 + size_cell_sign, size_cell * 8 + size_cell_sign,
                        width=2, outline=color1)

# Вывод цифр на доску
num = 8
for i in range(size_cell, size_cell*9, size_cell):
    canvas.create_text(size_cell_sign / 2, i, text=str(num), font=("Arial", 15))
    canvas.create_text(size_cell * 8 + size_cell_sign + size_cell_sign / 2, i, text=str(num), font=("Arial", 15))
    num -= 1

num = [8, 7, 6, 5, 4, 3, 2, 1]
char = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Вывод букв на доску
for i in range(1, 9):
    canvas.create_text(size_cell*i, 15, text=char[i-1], font=("Arial", 15))
    canvas.create_text(size_cell*i, size_cell*9-15, text=char[i-1], font=("Arial", 15))


def check():
    text.config(state='normal')
    text.delete(1.0, END)

    for i in range(len(chess)-1):
        for j in range(len(chess)):
            if i != j and i < j:
                if abs(chess[i][0] - chess[j][0]) == abs(chess[i][1] - chess[j][1]) \
                        or chess[i][0] == chess[j][0] or chess[i][1] == chess[j][1]:
                    chess_win.append([char[chess[i][0]], f'{num[chess[i][1]]}', char[chess[j][0]], f'{num[chess[j][1]]}'])

    if len(chess_win) == 0:
        text.insert(1.0, "Нет комбинаций")
    else:
        win_text = ""
        auxiliaryList = []
        for i in chess_win:
            if i not in auxiliaryList:
                auxiliaryList.append(i)
        for e in auxiliaryList:
            for i, j in enumerate(e):
                if i == 1:
                    win_text = win_text + str(j) + " => "
                elif i == len(e) - 1:
                    win_text = win_text + str(j) + "\n"
                else:
                    win_text = win_text + str(j) + ""
        text.insert(1.0, win_text)
    text.config(state='disabled')


queen = PhotoImage(file="queen.png")


def click(e, row, col):
    global chess_win
    if [row, col] in chess:
        canvas.delete(f"queen_{row}_{col}")
        del chess[chess.index([row, col])]
        chess_win = []
    else:
        chess.append([row, col])
        canvas.create_image(row * size_cell + size_cell_sign + 3, col * size_cell + size_cell_sign + 4, image=queen,
                            anchor="nw", tag=f"queen_{row}_{col}")
        canvas.tag_bind(f"queen_{row}_{col}", "<Button-1>", lambda event="", row=row, col=col: click(event, row, col))

    check()


root.mainloop()
