import tkinter as tk
import time


root = tk.Tk()
cells_number_by_height = 30
cells_number_by_width = 40
cell_size = 20
cells = [[0] * cells_number_by_width for i in range(cells_number_by_height)]
sums = 0


canvas = tk.Canvas(root,
                   height=cells_number_by_height*cell_size,
                   width=cells_number_by_width*cell_size,
                   bg='lightgrey')
canvas.pack(padx=5, pady=5)

btn_next_gen = tk.Button(root, text='Next generation')
btn_next_gen.pack()


btn_next_gen_100 = tk.Button(root, text='100 Next generation')
btn_next_gen_100.pack()


def draw_grid():
    for i in range(0, cell_size*cells_number_by_height, cell_size):
        canvas.create_line(0, i, cells_number_by_width*cell_size, i)
    for i in range(0, cell_size * cells_number_by_width, cell_size):
        canvas.create_line(i, 0, i, cells_number_by_height * cell_size)


def draw_cells():
    for i in range(cells_number_by_height):
        for j in range(cells_number_by_width):
            if cells[i][j] == 1:
                canvas.create_rectangle(j * cell_size,
                                        i * cell_size,
                                        j * cell_size + cell_size,
                                        i * cell_size + cell_size,
                                        fill='green')


def calc_sums():
    global sums
    sums = [[get_cell_sum(i, j) for j in range(cells_number_by_width)]
            for i in range(cells_number_by_height)]


def get_cell_sum(i, j):
    sum = 0
    if i > 0: sum += cells[i-1][j]  # up
    if i < cells_number_by_height-1: sum += cells[i+1][j]   # down
    if j > 0: sum += cells[i][j-1]  # left
    if j < cells_number_by_width-1: sum += cells[i][j+1]    # right
    if i > 0 and j > 0: sum += cells[i-1][j-1]  # left up
    if i < cells_number_by_height-1 and j > 0: sum += cells[i+1][j-1]    # left down
    if i > 0 and j < cells_number_by_width-1: sum += cells[i-1][j+1]    # right up
    if i < cells_number_by_height-1 and j < cells_number_by_width-1: sum += cells[i+1][j+1] # right down
    return sum


def draw_sums():
    for i in range(cells_number_by_height):
        for j in range(cells_number_by_width):
            if cells[i][j] == 0:
                canvas.create_text(j*cell_size+cell_size/2,
                                   i*cell_size+cell_size/2,
                                   text=str(sums[i][j]))


def generation():
    canvas.delete('all')
    draw_grid()
    draw_cells()
    calc_sums()
    draw_sums()


def next_generation():
    global sums, cells
    for i in range(cells_number_by_height):
        for j in range(cells_number_by_width):
            if cells[i][j] == 0 and sums[i][j] in [2, 3]:
                cells[i][j] = 1
            else:
                cells[i][j] = 0
    generation()


def next_100():
    timeout = 0.1
    for i in range(100):
        next_generation()
        root.update()
        time.sleep(timeout)


def click(e):
    global sums, cells
    if e.widget != canvas:
        return
    i, j = e.y // cell_size, e.x // cell_size
    cells[i][j] = 1
    generation()


generation()
btn_next_gen['command'] = next_generation
btn_next_gen_100['command'] = next_100
root.bind('<Button-1>', click)
root.mainloop()
