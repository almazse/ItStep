import tkinter as tk


class TicTacToeView:

    def __init__(self, master):
        self.master = master
        self.playground = tk.Canvas

    def create_window(self, width, height, header_s, rectangle):
        self.master.title("Крестики нолики")
        # окно по центру экрана
        self.master.geometry(f'+{self.master.winfo_screenwidth() // 2 - width // 2}+'
                             f'{self.master.winfo_screenheight() // 2 - (height + header_s) // 2}')
        self.master.resizable(False, False)  # запретить растягивать

        self.playground = tk.Canvas(width=rectangle * 3, height=rectangle * 3 + header_s, highlightthickness=0)
        self.playground.grid(row=0, column=0)

    def generate_playground(self, col, row, rectangle):
        self.playground.create_rectangle(col * rectangle, row * rectangle + rectangle,
                                         col * rectangle + rectangle, row * rectangle, tags=f"{row}_{col}",
                                         fill="white")
        # self.playground.tag_bind(f"{row}_{col}", "<Button-1>", lambda e="", rows=row, cols=col: click(e, rows, cols))

    def generate_statistic(self, rectangle, color, font):
        self.playground.create_text(40, rectangle * 3 + 10, text="X", anchor="nw", fill=color[0], font=(font, 20, "bold"))
        self.playground.create_text(30, rectangle * 3 + 50, text="player 1", anchor="nw", fill=color[0])

        player_line = self.playground.create_line(25, rectangle * 3 + 75, 75, rectangle * 3 + 75, fill=color[0], width=5)

        self.playground.create_text(rectangle * 3 / 2, rectangle * 3 + 30, text="vs", anchor="center", font=(font, 18))

        display_counter = self.playground.create_text(rectangle * 3 / 2, rectangle * 3 + 55,
                                                      text="0 / 0", anchor="center", font=(font, 10))

        self.playground.create_text(rectangle * 3 - 60, rectangle * 3 + 10, text="O", anchor="nw",
                                    fill=color[1], font=(font, 20, "bold"))
        self.playground.create_text(rectangle * 3 - 70, rectangle * 3 + 50, text="player 2", anchor="nw", fill=color[1])

    def generate_restart_btn(self, rectangle, font):
        # Кнопка перезапуска игры
        self.playground.create_text(rectangle * 3 / 2, rectangle * 3 + 90, text="\u21BA", anchor="center", fill="green",
                                    font=(font, 30, "bold"), tags="restart_button")
        # self.playground.tag_bind("restart_button", '<Button-1>', restart_game)
