try:
    uah = float(input("Ведите сумму в грн.: "))
except ValueError:
    print("\nОшибка! Некоректное значение!")
    uah = float(input("Ведите сумму в грн.: "))

while True:
    print(f'Баланс: {uah} грн.')
    print('1. Американские горки - 60 грн.\n2. Power Tower - 100 грн.\n'
          '3. Комната страха - 30 грн.\n4. Выход')

    try:
        choice = int(input("Выберите атракцион: "))
    except ValueError:
        print("\nОшибка! Некоректное значение!")
        choice = int(input("Выберите атракцион: "))

    if choice == 4:
        break

    if uah <= -1:
        print('На вашем счету не достаточно средств')
        break

    if choice == 3:
        uah = uah - 30
        print('\tКомната страха')
    if choice == 2:
        uah = uah - 100
        print('\tPower Tower')
    if choice == 1:
        uah = uah - 60
        print('\tАмериканские горки')


print('До новых встреч')