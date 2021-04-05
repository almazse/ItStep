import tkinter as tk

root = tk.Tk()
root.title("My GUI")
root.geometry("600x400+1070+0")  # (ширина)x(высота)+(отступ слева)+(отступ сверху)

is_blue = True
BLUE, YELLOW = "blue", "yellow"


label = tk.Label(root, text="СИНИЙ", width=50,
                 font=("Courier", "30"), bg=BLUE, fg=YELLOW)
label.pack(pady="20")

button = tk.Button(root, text="сделать желтый", font=("Arial", "40"))
button.pack()


def click():
    global is_blue
    if is_blue:
        label.config(bg=YELLOW, fg=BLUE, text="ЖЕЛТЫЙ")
        button.config(text="сделать синим")
    else:
        label.config(bg=BLUE, fg=YELLOW, text="СИНИЙ")
        button.config(text="сделать желтым")
    is_blue = not is_blue


button.config(command=click)

root.mainloop()
