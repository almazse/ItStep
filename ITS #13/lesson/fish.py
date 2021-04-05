
class Fish():

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def swim(self):
        print(f'hello i\'m {self.name} and i\'m swimming')


class Predator(Fish):

    def __init__(self, name, size):
        super().__init__(name, size)

    def eats(self):
        print(f'My eats: fish')


class Peaceful(Fish):
    def __init__(self, name, size):
        super().__init__(name, size)

    def eats(self):
        print(f'My eats: seaweed')


if __name__ == '__main__':
    fish = Fish("nemo", 2.2)
    fish.swim()
   
    fish_predator = Predator("Shark", 5)
    fish_predator.swim()
    fish_predator.eats()

    fish_predator = Peaceful("Gold", 5)
    fish_predator.swim()
    fish_predator.eats()
