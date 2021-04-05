import tkinter as tk

FONT = ("Arial", 25)
FONT_BTN = ("Courier", 14)
BG_BTN = "#1f2125"
FG_BTN = "white"
number_1 = ""
number_2 = ""
result = 0
action = ""
history = ""

root = tk.Tk()
root.title("Калькулятор")

root.config(bg="#2c2f33")
root.resizable(width=False, height=False)

labelHistory = tk.Entry(root, width=26, font=("Arial", 10), disabledbackground="#2c2f33",
                        disabledforeground="white", relief="flat", justify="right", state='disabled')
labelHistory.grid(row=0, column=0, columnspan=5)

label = tk.Entry(root, width=12, font=FONT, disabledbackground="#2c2f33", disabledforeground="white", relief="flat",
                 justify="right")
label.insert(0, 0)
label.config(state='disabled')
label.grid(row=1, column=0, columnspan=5)


btn_seven = tk.Button(root, text="7", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_seven.grid(row=2, column=0, pady=2, padx=2)

btn_eight = tk.Button(root, text="8", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_eight.grid(row=2, column=1, pady=2, padx=2)

btn_nine = tk.Button(root, text="9", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_nine.grid(row=2, column=2, pady=2, padx=2)

btn_split = tk.Button(root, text="/", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_split.grid(row=2, column=3, pady=2, padx=2)

btn_clear = tk.Button(root, text="C", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_clear.grid(row=2, column=4, pady=2, padx=2)


btn_four = tk.Button(root, text="4", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_four.grid(row=3, column=0, pady=2, padx=2)

btn_five = tk.Button(root, text="5", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_five.grid(row=3, column=1, pady=2, padx=2)

btn_six = tk.Button(root, text="6", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_six.grid(row=3, column=2, pady=1, padx=1)

btn_multiply = tk.Button(root, text="*", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_multiply.grid(row=3, column=3, pady=1, padx=1)

btn_deg = tk.Button(root, text="**", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_deg.grid(row=3, column=4, pady=1, padx=1)


btn_one = tk.Button(root, text="1", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_one.grid(row=4, column=0, pady=1, padx=1)

btn_two = tk.Button(root, text="2", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_two.grid(row=4, column=1, pady=1, padx=1)

btn_three = tk.Button(root, text="3", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_three.grid(row=4, column=2, pady=1, padx=1)

btn_minus = tk.Button(root, text="-", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_minus.grid(row=4, column=3, pady=1, padx=1)

btn_return = tk.Button(root, text="=", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=3, relief="flat")
btn_return.grid(row=4, column=4, rowspan=2, pady=1, padx=1)


btn_zero = tk.Button(root, text="0", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=7, height=1, relief="flat")
btn_zero.grid(row=5, column=0, columnspan=2)

btn_dot = tk.Button(root, text=".", font=FONT_BTN, bg=BG_BTN, fg=FG_BTN, width=3, height=1, relief="flat")
btn_dot.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", font=FONT_BTN, bg="#174ea6", fg=FG_BTN, width=3, height=1, relief="flat")
btn_plus.grid(row=5, column=3)


def insert_label(res):
    # запись в метку
    label.config(state='normal')
    label.delete(0, "end")
    label.insert(0, res)
    label.config(state='disabled')


def insert_history(num):
    # запись в метку истории
    labelHistory.config(state='normal')
    labelHistory.delete(0, "end")
    labelHistory.insert(0, str(num))
    labelHistory.config(state='disabled')


def calculate(arg_action):
    global action
    global number_1
    global number_2
    global result
    global history

    if not action:
        action = arg_action

    if not history:
        history = label.get()

    if not number_2:
        number_2 = label.get()
        number_1 = ""
    elif number_1:
        if action == "+":
            history = history + " + " + str(number_1)
            result = float(number_2) + float(number_1)
        elif action == "-":
            history = history + " - " + str(number_1)
            result = float(number_2) - float(number_1)
        elif action == "*":
            history = history + " * " + str(number_1)
            result = float(number_2) * float(number_1)
        elif action == "/":
            history = history + " / " + str(number_1)
            result = float(number_2) / float(number_1)
        elif action == "**":
            history = history + " ** " + str(number_1)
            result = float(number_2) ** float(number_1)

        number_2 = result
        number_1 = ""

        if result.is_integer():
            result = int(result)

        insert_label(result)

    if arg_action == "Return":
        action = ""
        history = ""
    else:
        action = arg_action

    insert_history(history + " " + action)


def press_btn_number(event):
    global number_1

    number_1 = str(number_1) + event.char
    insert_label(number_1)

def press_btn_dot(event):
    global number_1

    if '.' not in number_1:
        number_1 = str(number_1) + "."
        insert_label(number_1)


def press_btn(event):
    if event.char != "\r":
        calculate(event.char)
    else:
        calculate("Return")


root.bind("+", press_btn)
root.bind("-", press_btn)
root.bind("*", press_btn)
root.bind("/", press_btn)
root.bind(".", press_btn_dot)
root.bind("<Return>", press_btn)
root.bind(1, press_btn_number)
root.bind(2, press_btn_number)
root.bind(3, press_btn_number)
root.bind(4, press_btn_number)
root.bind(5, press_btn_number)
root.bind(6, press_btn_number)
root.bind(7, press_btn_number)
root.bind(8, press_btn_number)
root.bind(9, press_btn_number)
root.bind(0, press_btn_number)


def click_seven():
    global number_1
    global result

    number_1 = str(number_1) + "7"
    insert_label(number_1)


btn_seven.config(command=click_seven)


def click_eight():
    global number_1
    global result

    number_1 = str(number_1) + "8"
    insert_label(number_1)


btn_eight.config(command=click_eight)


def click_nine():
    global number_1
    global result

    number_1 = str(number_1) + "9"
    insert_label(number_1)


btn_nine.config(command=click_nine)


def click_split():
    calculate("/")


btn_split.config(command=click_split)


def click_clear():
    global action
    global number_1
    global number_2
    global result
    global history

    action = ""
    number_1 = ""
    number_2 = ""
    result = ""
    history = ""

    insert_history(history)
    insert_label(0)


btn_clear.config(command=click_clear)


def click_four():
    global number_1
    global result

    number_1 = str(number_1) + "4"
    insert_label(number_1)


btn_four.config(command=click_four)


def click_five():
    global number_1
    global result

    number_1 = str(number_1) + "5"
    insert_label(number_1)


btn_five.config(command=click_five)


def click_six():
    global number_1
    global result

    number_1 = str(number_1) + "6"
    insert_label(number_1)


btn_six.config(command=click_six)


def click_multiply():
    calculate("*")


btn_multiply.config(command=click_multiply)


def click_deg():
    calculate("**")


btn_deg.config(command=click_deg)


def click_one():
    global number_1
    global result

    number_1 = str(number_1) + "1"
    insert_label(number_1)


btn_one.config(command=click_one)


def click_two():
    global number_1
    global result

    number_1 = str(number_1) + "2"
    insert_label(number_1)


btn_two.config(command=click_two)


def click_three():
    global number_1
    global result

    number_1 = str(number_1) + "3"
    insert_label(number_1)


btn_three.config(command=click_three)


def click_minus():
    calculate("-")


btn_minus.config(command=click_minus)


def click_return():
    calculate("Return")


btn_return.config(command=click_return)


def click_zero():
    global number_1
    global result

    number_1 = str(number_1) + "0"
    insert_label(number_1)


btn_zero.config(command=click_zero)


def click_dot():
    global number_1

    if '.' not in number_1:
        number_1 = str(number_1) + "."
        insert_label(number_1)


btn_dot.config(command=click_dot)


def click_plus():
    calculate("+")


btn_plus.config(command=click_plus)

root.mainloop()
