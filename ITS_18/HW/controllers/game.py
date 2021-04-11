from ITS_18.HW.views.tkinter_view import TkinterView
from ITS_18.HW.models.cells import Cells
import tkinter as tk
import time


class LifeGame:
    def __init__(self):
        self.cells_number_by_height = 30
        self.cells_number_by_width = 40
        self.cell_size = 20
        self.cells = Cells()


        self.view = TkinterView(self.cells_number_by_height, self.cells_number_by_width, self.cell_size)

    def start(self):
        self._draw_grid()

    def _draw_grid(self):
        for i in range(0, self.cell_size * self.cells_number_by_height, self.cell_size):
            self.view.create_line_vertical(i)

