class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'sqeark'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals):
    for a in animals:
        print(a.make_sound())


if __name__ == '__main__':
    animals = [Lion('lion'), Snake('snake'), Mouse('mouse')]
    animal_sound(animals)