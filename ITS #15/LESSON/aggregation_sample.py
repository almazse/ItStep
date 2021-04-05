from decimal import Decimal


class Salary:
    def __init__(self, pay: Decimal):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:

    def __init__(self, name: str, pay: Salary, bonus: Decimal):
        self._name = name
        self._pay = pay
        self._bonus = bonus

    def annual_salaty(self):
        annual_salary = self._pay.get_total() + self._bonus
        print(f'Annual salary of {self._name} = {annual_salary}')


if __name__ == '__main__':
    salary_programmer = Salary(Decimal(2200))
    john = Employee('John', salary_programmer, Decimal(1500))
    john.annual_salaty()