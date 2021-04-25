from dataclasses import dataclass, field


@dataclass
class TicTacToeModel:
    WIDTH: int = 300
    HEIGHT: int = 300
    HEADER_S: int = 120
    FONT: str = "Comic Sans MS"
    RECTANGLE: int = 70
    cell = [["", "", ""], ["", "", ""], ["", "", ""]]
    game_over: bool = False
    COLOR = ["red", "blue"]
    player: str = "X"
    player_line: str = ""
    counter = [0, 0]
    progress_counter: int = 0
