from random import *
from datetime import *


class Passport:

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.city = city
        self.gen = gen.upper()
        self.birth_date = birth_date

        self.authority = randint(1111, 9999)
        self.__number = randint(100000000, 999999999)
        self.create_date = datetime.today().strftime('%d-%m-%Y')

    def __str__(self):
        return f'Passport: {self.name} {self.surname}'

    def print(self):
        print(f"Passport info:\n\
              Name: {self.name}\n\
              Surname: {self.surname}\n\
              Patronymic: {self.patronymic}\n\
              City: {self.city}\n\
              Gender: {self.gen}\n\
              Birth date: {self.birth_date}\n\
              Authority: {self.authority}\n\
              Number: {self.__number}\n\
              Date: {self.create_date}")


class ForeignPassport(Passport):

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        super().__init__(name, surname, patronymic, gen, city, birth_date)

        self.__number = randint(100000000, 999999999)

        self.visa = []

    def new_visa(self, country, end_time):
        self.visa.append({country: end_time})

    def _print(self):
        print(f"Passport info:\n\
              Name: {self.name}\n\
              Surname: {self.surname}\n\
              Patronymic: {self.patronymic}\n\
              City: {self.city}\n\
              Gender: {self.gen}\n\
              Birth date: {self.birth_date}\n\
              Number: {self.__number}")
        print('Visa info: ')
        for item in self.visa:
            print('\t',list(item.keys())[0], ':', list(item.values())[0])


Bob = Passport('Bob', 'Bock', 'Borisovich', 'm', 'London', '25.06.2016')
print(Bob)
Bob.print()

Bill = ForeignPassport('Bill', 'Bock', 'Borisovich', 'm', 'London', '25.06.2016')
Bill.new_visa('Poland', '01.09.2021')
Bill._print()
# print(Bob.authority, Bob.number)


class Add:

    def __init__(self, num):
        self.numb = num

    def __add__(self, b):
        self.numb = self.numb * b


a = Add(5)
b = Add(7)
# a.__add__(5)

print(a.numb)
print(a.numb + b.numb)