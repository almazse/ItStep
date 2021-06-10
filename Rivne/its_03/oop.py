# абстрактность
# наследование
# инкапсуляция
# полиморфизм


#             фигура
#             построение()
#             line_color
#             line_type
#             fill
#
#
# круг            квадрат         треугольник
# построение()    построение()    построение()

class Person:
    # _name = 'no name'
    # __age = 0

    def __init__(self, name='no name', age=0):
        self._name = name
        self.__age = age

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
        print(f'My name is {self._name}')
        print(f'I am {self.__age}')


person1 = Person('Bob', 35)
# print(isinstance(person1, Person))
# person1._name = 'Bob'
# person1.set_age(35)

# print(person1.get_age())
person1.age = 36
print(person1.age)

# person2 = Person()
# person2._name = 'Kate'
# person2.set_age(30)

person1.description_of_person()
# person2.description_of_person()
