import tkinter as tk

root = tk.Tk()
root.title("Pack - f..k")
# root.geometry("600x400+1070+0")  # (ширина)x(высота)+(отступ слева)+(отступ сверху)

label_1 = tk.Label(root, text="#1", width=7, height=3,
                 font=("Courier", "30"), bg="blue", fg="white")
label_1.pack(side="left", padx=20, pady="20")

label_2 = tk.Label(root, text="#2", width=7, height=3,
                 font=("Courier", "30"), bg="red", fg="white")
label_2.pack(padx=20, pady="20")

label_3 = tk.Label(root, text="#3", width=7, height=3,
                 font=("Courier", "30"), bg="green", fg="white")
label_3.pack(side="left", padx=20, pady="20")

label_4 = tk.Label(root, text="#4", width=7, height=3,
                 font=("Courier", "30"), bg="purple", fg="white")
label_4.pack(padx=20, pady="20")

root.mainloop()
