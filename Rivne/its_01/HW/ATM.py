print('БАНКОМАТ')

try:
    pin = int(input("Ведите пин-код: "))
except ValueError:
    print("\nОшибка! Некоректное значение!")
    pin = int(input("Ведите пин-код: "))

if pin == 1234:
    balance = 2000.22
    while True:
        print('1. Посмотреть баланс\n2. Снять Деньги\n3. Выход')

        try:
            choice = int(input("Сделайте выбор: "))
        except ValueError:
            print("\nОшибка! Некоректное значение!")
            choice = int(input("Сделайте выбор: "))
        if choice == 1:
            print(f"Баланс {balance} грн.")
        if choice == 2:
            try:
                summa = float(input("Сума для снятия: "))
            except ValueError:
                print("\nОшибка! Некоректное значение!")
                summa = float(input("Сума для снятия: "))
            if balance - summa >= 0:
                balance = balance - summa
                print("\nУспешно! Возьмите деньги")
            else:
                print("\nНедостаточно средсв")
        if choice == 3:
            print("Досвиданья")
            break

else:
    print('Неверный пин-код')
