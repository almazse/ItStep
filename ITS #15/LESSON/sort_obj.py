class Kitty:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        print("Meow!")

    def __lt__(self, other):
        return self._age < other._age
