import tkinter as tk


class TkinterView:
    def __init__(self, cells_number_by_height, cells_number_by_width, cell_size):
        self.cells_number_by_height = cells_number_by_height
        self.cells_number_by_width = cells_number_by_width
        self.cell_size = cell_size
        self.root = tk.Tk()



        self.canvas = tk.Canvas(self.root,
                           height=cells_number_by_height * cell_size,
                           width=cells_number_by_width * cell_size,
                           bg='lightgrey')
        self.canvas.pack(padx=5, pady=5)

        btn_next_gen = tk.Button(self.root, text='Next generation')
        btn_next_gen.pack()

        btn_next_gen_100 = tk.Button(self.root, text='100 Next generation')
        btn_next_gen_100.pack()

    def create_line_vertical(self, i):
        self.canvas.create_line(0, i, self.cells_number_by_width*self.cell_size, i)
        self.mainloop()




