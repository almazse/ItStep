try:
    cost = float(input("Введите цену одной минуты (грн.): "))
except ValueError:
    print("\nОшибка! Некоректное значение!")
    cost = float(input("Введите цену одной минуты: (грн.)"))

try:
    duration = int(input("Введите длительность разговора (мин.): "))
except ValueError:
    print("\nОшибка! Некоректное значение!")
    duration = int(input("Введите длительность разговора (мин.): "))

print(f'Стоимость звонка: {cost*duration} грн.')
