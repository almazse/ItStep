from views.tkinter_view import TkinterView
from models.cells import Cells
from models.model import Data
import tkinter as tk


class LifeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.data = Data()
        self.view = TkinterView(self.root)
        self.cells = Cells()
        self.cells.get_cells()

    def start(self):
        self.view.create_canvas(self.data.cells_number_by_height, self.data.cell_size, self.data.cells_number_by_width)
        self._draw_grid()
        self.view.create_button()
        self.root.mainloop()

    def _draw_grid(self):
        for i in range(0, self.data.cell_size * self.data.cells_number_by_height, self.data.cell_size):
            self.view.create_line_vertical(i, self.data.cells_number_by_width, self.data.cell_size)
        for i in range(0, self.data.cell_size * self.data.cells_number_by_width, self.data.cell_size):
            self.view.create_line_horizontal(i, self.data.cells_number_by_height, self.data.cell_size)

    def click(self, e, canvas):
        global sums, cells
        if e.widget != canvas:
            return
        i, j = e.y // self.data.cell_size, e.x // self.data.cell_size
        self.cells[i][j] = 1
        # generation()
