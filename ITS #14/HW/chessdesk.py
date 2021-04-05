import math


class ChessDesk:
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight

        if isinstance(self._height, str) or isinstance(self._weight, str):
            self.print_error_msg()
        elif self._height is None and self._weight is None:
            self.print_error_msg()
        elif self._height <= 1:
            self.print_error_msg()
        elif self._height and self._weight is None:
            self._weight = self._height
            self.get_chess_desk()
        elif self._height and self._weight:
            self.get_chess_desk()

    @staticmethod
    def print_error_msg():
        print("There didn't put numbers or values are too small"
              ', please enter to '
              "create square desk HEIGHT.\n"
              "To create rectangular desk "
              "enter first HEIGHT and second WEIGHT. ", end="")

    def get_chess_desk(self):
        height = math.ceil(self._height)
        weight = math.ceil(self._weight)

        for col in range(height):
            if col % 2 == 0:
                for row in range(weight):
                    if row % 2 == 0:
                        print(f"*", end="")
                    else:
                        print(f" ", end="")
            else:
                for row in range(weight):
                    if row % 2 == 0:
                        print(f" ", end="")
                    else:
                        print(f"*", end="")
            print()
