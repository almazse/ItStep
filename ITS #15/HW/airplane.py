class Airplane:
    def __init__(self, type, passagers):
        self.type = type
        self.passagers = passagers

    def __eq__(self, other):
        """
            :type other: Airplane
        """
        if other.type == self.type:
            return "These planes are the same"
        return "These planes are different"

    def __le__(self, other):
        """
            :type other: Airplane
        """
        if other.passagers > self.passagers:
            return f"{other.type} ({other.passagers}) it has more passengers than {self.type} ({self.passagers})"
        elif other.passagers < self.passagers:
            return f"{other.type} ({other.passagers}) has fewer passengers than {self.type} ({self.passagers})"
        return f"{other.type} ({other.passagers}) has as many passengers as {self.type} ({self.passagers})"

    def __lt__(self, other):
        """
            :type other: Airplane
        """
        if other.passagers > self.passagers:
            return f"{other.type} ({other.passagers}) it has more passengers than {self.type} ({self.passagers})"
        return f"{other.type} ({other.passagers}) has fewer passengers than {self.type} ({self.passagers})"

    def __add__(self, other):
        """
            :type other: Airplane
        """
        return f'Now the capacity in the cabin: {self.passagers + other} passagers'

    def __iadd__(self, other):
        """
            :type other: Airplane
        """
        self.passagers += other
        return f'Now the capacity in the cabin: {self.passagers} passagers'

    def __sub__(self, other):
        """
            :type other: Airplane
        """
        return f'Now the capacity in the cabin: {self.passagers - other} passagers'

    def __isub__(self, other):
        """
            :type other: Airplane
        """
        self.passagers -= other
        return f'Now the capacity in the cabin: {self.passagers} passagers'


if __name__ == '__main__':
    boeing += 25
    print(boeing)

    super_jet -= 25
    print(super_jet)




