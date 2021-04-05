day, month, year = input("Введите дату формате день.месяц.год: ").split(".")
day, month, year = int(day), int(month), int(year)

#проверяем високостный ли год
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    february = 29
else:
    february = 28

if month == 12 and day == 31:
    day, month, year = 1, 1, year+1
elif month != 2 and month % 2 == 0 and day + 1 > 31:
    day, month, year = 1, month+1, year
elif month != 2 and month % 2 != 0 and day + 1 > 30:
    day, month, year = 1, month+1, year
elif month == 2 and day + 1 > february:
    day, month, year = 1, month+1, year
else: 
    day, month, year = day + 1, month, year
    
print(f"{day:02}.{month:02}.{year}")