class Person:
    """
    Person class
    """

    def __init__(self, name='no name', age=0):
        self._name = name
        self.__age = age
        self.__address = 'n/a'

    def set_address(self, addr):
        self.__address = addr

    def address(self):
        return self.__address

    def set_age(self, a):
        self.__age = a

    def get_age(self):
        return self.__age

    @property
    def age(self):
        return self.__age

    # @age.getter
    # def age(self):
    #     return self.__age

    @age.setter
    def age(self, a):
        if a > 0:
            self.__age = a
        else:
            print('incorrect data!')

    def description_of_person(self):
        print('----------------------')
        print(f'| My name is {self._name}')
        print(f'| I am {self.__age}')
        print(f'| I leave in {self.__address}')