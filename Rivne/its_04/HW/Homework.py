from random import *
from datetime import *


class Passport:

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.city = city
        self.gen = gen.upper()
        self.birth_date = datetime.strptime(birth_date, "%d.%m.%Y").strftime("%d-%m-%Y")

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

    def get_birth_date(self):
        return f"{self.name}, born {self.birth_date}"


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
            print(f'\t{list(item.keys())[0]}: {list(item.values())[0]}')

    def get_country_visited(self):
        print('Visited countries:\n\t', end='')
        countries = []
        for item in self.visa:
            if list(item.keys())[0] not in countries:
                countries.append(list(item.keys())[0])

        return countries

    def get_pending_visa(self):
        print('Information about unfinished visas:')
        for item in self.visa:
            dateVisa = datetime.strptime(list(item.values())[0], "%d.%m.%Y")
            dateToday = datetime.today()
            if dateVisa > dateToday:
                print(f'\t{list(item.keys())[0]}: {list(item.values())[0]}')


Bob = Passport('Bob', 'Bock', 'Borisovich', 'm', 'London', '25.06.2016')
print(Bob)
Bob.print()

Bill = ForeignPassport('Bill', 'Bock', 'Borisovich', 'm', 'London', '25.06.2016')
Bill.new_visa('Poland', '01.09.2021')
Bill.new_visa('Ukraine', '01.09.2020')
Bill.new_visa('Ukraine', '22.11.2024')
Bill._print()

print(*Bill.get_country_visited(), sep=', ')
print()
Bill.get_pending_visa()

print()
print(Bill.get_birth_date())
# print(Bob.authority, Bob.number)

