class Resistor:
    def __init__(self, resistance: int):
        self.resistance = resistance

    def __str__(self):
        return f'Resistance = {self.resistance}'


class SeriesResistance:
    def __init__(self, *resistors):
        self.resistance = sum([resistor.resistance for resistor in resistors])

    def __str__(self):
        return f'Resistance = {self.resistance}'


class ParallelResistance:
    def __init__(self):
        self.resistance = 1.0 / sum([1.0/resistor.resistance for resistor])

    def __str__(self):
        return f'Resistance = {self.resistance}'