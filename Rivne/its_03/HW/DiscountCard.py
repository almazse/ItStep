from datetime import date
from random import randint


class DiscountCard:

    def __init__(self):
        self.number = randint(100000, 999999)
        self.__discount = 1
        self.__amount = 0.0
        d = date.today()
        self.date = f'{d.day:02}/{d.month:02}/{d.year}'

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, purchase):
        self.__amount += purchase

    @property
    def discount(self):
        return self.__discount

    def discount_calculate(self):
        self.__discount = int(self.__amount // 1000 + 1)


if __name__ == '__main__':
    discountCard = DiscountCard()
    while True:
        print('1. Купить товар\n'
              '2. Показать текущую скидку\n'
              '3. Показать сколько до следующей скидки\n'
              '0. Выход')
        try:
            choice = int(input('Выберите пункт меню: '))

            if choice == 0:
                print('До новых встреч')
                break
            elif choice == 1:
                amount = input('Введите сумму покупки: ')
                card = input('Использовать карту(Да): ')
                if card == '' or card == 'Да' or card == 'да':
                    discountCard.amount = float(amount)
                    discountCard.discount_calculate()
                    print('*** Спасибо за покупку ***')
                elif card == 'Нет' or card == 'нет':
                    print('*** Спасибо за покупку ***')

            elif choice == 2:
                print(f'Текущая скидка: {discountCard.discount} %')
            elif choice == 3:
                print(f'До следующей скидки: {1000 - (discountCard.amount % 1000)} грн.')
            else:
                print('Введите значение от 0 до 3')
                continue

        except ValueError:
            print('ОШИБКА! Неверное значение')
