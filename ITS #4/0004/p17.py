import tkinter as tk

FONT = ("Courier", 30)

root = tk.Tk()
root.title("Counter")

entry_num = tk.Entry(root, width=4, font=FONT)
entry_num.insert(0, 0)
entry_num.grid(row=0, column=0, columnspan=2)

btn_plus = tk.Button(root, text="+", font=FONT, bg="#7FFFD4", width=5)
btn_plus.grid(row=1, column=0, pady=20, padx=5)

btn_minus = tk.Button(root, text="-", font=FONT, bg="#7FFF00", width=5)
btn_minus.grid(row=1, column=1, pady=20, padx=5)


def click_minus():
    counter = int(entry_num.get()) - 1

    if counter < 0:
        counter = 0

    entry_num.delete(0, "end")
    entry_num.insert(0, counter)


def click_plus():
    counter = int(entry_num.get()) + 1

    entry_num.delete(0, "end")
    entry_num.insert(0, counter)


btn_minus.config(command=click_minus)
btn_plus.config(command=click_plus)

root.mainloop()
