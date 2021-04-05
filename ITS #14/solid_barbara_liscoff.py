class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def make_sound(self):
        pass

    def leg_count(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'

    def leg_count(self):
        return 4


class Mouse(Animal):
    def make_sound(self):
        return 'sqeark'

    def leg_count(self):
        return 4


class Snake(Animal):
    def make_sound(self):
        return 'hiss'

    def leg_count(self):
        return 0


class Pigeon(Animal):
    def make_sound(self):
        return 'some voice'

    def leg_count(self):
        return 2



# def animal_leg_count(animals):
#     for a in animals:
#         if isinstance(a, Lion):
#             print(lion_leg_count(a))
#         if isinstance(a, Mouse):
#             print(mouse_leg_count(a))
#         if isinstance(a, Snake):
#             print(snake_leg_count(a))


def animal_leg_count(animals):
     for a in animals:
         print(a.leg_count())


if __name__ == '__main__':
    animals = [Lion('Lion'), Snake('Snake'), Mouse('Mouse'), Pigeon('Pigeon')]
    animal_leg_count(animals)