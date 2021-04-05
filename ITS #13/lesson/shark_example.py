class Shark:
    def __init__(self):
        pass

    def swim(self):
        print('the shark is swimming')

    def eat(self, meal):
        print(f'the shark is eating {meal}')


class Dog:
    def __init__(self, name):
        self.name = name
        print(f'Dog {name} is created')

    def voice(self):
        print(f'Dogs {self.name} gav, gav')


if __name__ == '__main__':
    shark = Shark()
    shark.swim()

    shark2 = Shark()
    shark2.swim()
    shark2.eat('meat')

    print()

    dog = Dog("Bobby")
    dog2 = Dog("Billy")
    dog3 = Dog("Pluto")

    dogs = [dog, dog2, dog3,]
    [dog.voice() for dog in dogs]

