class Boy:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Boy [name={self.name}, age={self.age}]'

    def introduce(self):
        print(f'Hi, I am {self.name} and I\'m {self.age} y.o.')


if __name__ == '__main__':
    misha = Boy('Misha', 29)
    misha.introduce()
    misha.age = 19

    print(misha)
