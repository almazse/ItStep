import tkinter as tk
from controllers.game import LifeGame


class TkinterView:
    def __init__(self, root):
        self.root = root
        self.cells_number_by_height = 30
        self.cells_number_by_width = 40
        self.cell_size = 20
        self.canvas = tk.Canvas()

    def create_canvas(self, cells_number_by_height, cell_size, cells_number_by_width):
        self.canvas = tk.Canvas(self.root,
                                height=cells_number_by_height * cell_size,
                                width=cells_number_by_width * cell_size,
                                bg='lightgrey')
        self.canvas.pack(padx=5, pady=5)

    def create_button(self):
        btn_next_gen = tk.Button(self.root, text='Next generation')
        btn_next_gen.pack()

        btn_next_gen_100 = tk.Button(self.root, text='100 Next generation')
        btn_next_gen_100.pack()

    def create_line_vertical(self, i, cells_number_by_width, cell_size):
        self.canvas.create_line(0, i, cells_number_by_width * cell_size, i)

    def create_line_horizontal(self, i, cells_number_by_height, cell_size):
        self.canvas.create_line(i, 0, i, cells_number_by_height * cell_size)





