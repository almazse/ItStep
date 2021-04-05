# Tkinter GUI (graphical user interface)

import tkinter as tk

root = tk.Tk()
root.title("My GUI")
root.geometry("600x400+1070+0") # (ширина)x(высота)+(отступ слева)+(отступ сверху)

label = tk.Label(root, text="Это надпись", width=30,
                 font=("Courier", "30"), bg="white", fg="red")
label.pack(pady="20")

button = tk.Button(root, text="Жми сюда!", font=("Arial", "40"))
button.pack()


def click():
    # print("CLICK!")
    label.config(text="Зачем ты нажал кнопку?")


button.config(command=click)

root.mainloop()
