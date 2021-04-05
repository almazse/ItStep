from tkinter import *
import random
import os.path

COLOR_B = "black"
COLOR_G = "#00ff00"
FILENAME = "data.txt"
WIDTH = 480
HEIGHT = 270


# Нажатие на кнопку create
def click_create():
    text.config(state='normal')
    text.delete(1.0, END)
    n = entry.get()
    if n.isdigit():
        transactions = []
        for i in range(int(n)):
            # генерируем 3 рандомных числа, 3 буквы и сумму
            transactions.append(f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
                                f"{chr(random.randrange(97, 123))}{chr(random.randrange(97, 123))}"
                                f"{chr(random.randrange(97, 123))} {random.uniform(100000, 1000000):.2f}")

        with open(FILENAME, "w") as f:
            f.write("\n".join(transactions))
        text.insert(1.0, f"{n} транзакций запиано в файл {FILENAME}\n")
    else:
        text.insert(1.0, "Нужно ввести целое число\n")
    text.config(state='disabled')


def click_read():
    text.config(state='normal')
    text.delete(1.0, END)

    # Проверка существования файла
    if not os.path.isfile(FILENAME):
        text.insert(1.0, f"Файл с данными не найден")
        text.config(state='disabled')
        return

    with open(FILENAME, "r") as f:
        max_sum = 0.0
        max_sum_code = ""
        max_ln_num = 0
        sum_code7 = []
        for i, line in enumerate(f.readlines()):
            line = line.strip().split()

            if line[0][0] == "7":
                sum_code7.append(float(line[1]))

            # Находим максимальную сумму
            if max_sum < float(line[1]):
                max_ln_num = i
                max_sum_code = line[0]
                max_sum = float(line[1])

    text.insert(1.0,
                f"\nМаксимальная сумма: {max_sum}\nКод транзкакции: {max_sum_code}\nНомер строки: {max_ln_num + 1}")
    if len(sum_code7) == 0:
        text.insert(1.0, f"Транзакции, код которых\nначинаеться на '7': "
                         f"Не найдены")
    else:
        text.insert(1.0, f"Средняя сумма для транзакций, код которых\nначинаеться на '7': "
                         f"{sum(sum_code7) / len(sum_code7):.2f}")
    text.config(state='disabled')


def remove_file():
    text.config(state='normal')
    text.delete(1.0, END)
    if os.path.isfile(FILENAME):
        os.remove(FILENAME)
        text.insert(1.0, f"Файл {FILENAME} удален")
    else:
        text.insert(1.0, f"Файл с данными не найден")
    text.config(state='disabled')


root = Tk()
# Оформление формы
root.config(bg=COLOR_B)
root.resizable(False, False)  # запретить растягивать
root.geometry(f'+{root.winfo_screenwidth() // 2 - WIDTH // 2}+'
              f'{root.winfo_screenheight() // 2 - HEIGHT // 2}')
root.title("Генератор транзакций")

Label(root, font=("Arial", 15), text="Введите количество транзакций: ", bg=COLOR_B, fg=COLOR_G) \
    .grid(row=1, column=0, columnspan=2, padx=10, sticky="nswe")

entry = Entry(root, width=30, font=("Arial", 20), bg=COLOR_B, fg=COLOR_G, highlightthickness=2,
              highlightbackground=COLOR_G, highlightcolor=COLOR_G, insertbackground=COLOR_G, relief="flat")
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nswe")

btn_create = Button(root, text="Create", width=15, font=("Arial", 15), bg=COLOR_G, fg=COLOR_B,
                    activebackground=COLOR_G, command=click_create)
btn_create.grid(row=3, column=0, padx=10, sticky="nswe")

btn_read = Button(root, text="Read", width=15, font=("Arial", 15), bg=COLOR_G, fg=COLOR_B,
                  activebackground=COLOR_G, command=click_read)
btn_read.grid(row=3, column=1, padx=10, sticky="nswe")

text = Text(root, width=40, height=5, bg=COLOR_B, fg=COLOR_G, highlightthickness=2, highlightbackground=COLOR_G,
            highlightcolor=COLOR_G, insertbackground=COLOR_G, relief="flat", state='disabled', font=("Arial", 15))
text.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nswe")

del_file = Button(root, text="Удалить файл c данными", font=("Arial", 15), bg="red", fg=COLOR_B,
                  activebackground="red", relief="flat", command=remove_file)
del_file.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nswe")

root.mainloop()
