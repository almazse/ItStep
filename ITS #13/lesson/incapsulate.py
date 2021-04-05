class Boy:
    adulthood_age = 18

    @staticmethod
    def describe():
        print('All boys are good!')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def grow(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def __str__(self):
        return f'Boy [name={self.__name}, age={self.__age}]'

    def introduce(self):
        print(f'Hi, I am {self.__name} and I\'m {self.__age} y.o.'
              f'{self.adulthood_age}')


if __name__ == '__main__':
    misha = Boy('misha', 29)
    # misha.__name
    misha.introduce()

    misha.grow()
    print(misha.get_name())
    print(misha.get_age())
    misha.set_name('vasya')
    print(misha)

    Boy.describe()
    print(Boy.adulthood_age)
    misha.describe()
    print(misha.adulthood_age)
