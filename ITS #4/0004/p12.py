import tkinter as tk
from p13 import get_solution_quad_eq

FONT = ("Courier", 30)

root = tk.Tk()
root.title("Quadratic Equations Solver")
root.geometry("700x400")  # (ширина)x(высота)+(отступ слева)+(отступ сверху)

tk.Label(root, text="x\u00b2 + ", font=FONT).grid(row=0, column=1)
tk.Label(root, text="x + ", font=FONT).grid(row=0, column=3)
tk.Label(root, text="= 0", font=FONT).grid(row=0, column=5)

entry_a = tk.Entry(root, width=4, font=FONT)
entry_a.insert(0, "1.0")
entry_a.grid(row=0, column=0, padx=10, pady=10)

entry_b = tk.Entry(root, width=4, font=FONT)
entry_b.insert(0, "2.0")
entry_b.grid(row=0, column=2, padx=10, pady=10)

entry_c = tk.Entry(root, width=4, font=FONT)
entry_c.insert(0, "-3.0")
entry_c.grid(row=0, column=4, padx=10, pady=10)

btn_slovo = tk.Button(root, text="Slove Equation", font=FONT, width=27)
btn_slovo.grid(row=1, column=0, columnspan=6, pady=20)

label_result = tk.Label(root, text="...", font=FONT, width=27,
                        height=3, bg="#00FFFF")
label_result.grid(row=2, column=0, columnspan=6, pady=20)

def click():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    res = get_solution_quad_eq(a, b, c)

    label_result.config(text=res)

btn_slovo.config(command=click)

root.mainloop()
