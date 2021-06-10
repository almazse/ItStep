import requests
from pprint import pprint

URL = 'https://api.covid19api.com/summary'
covid19 = requests.get(URL)
covid19_global = covid19.json()["Global"]
covid19 = covid19.json()["Countries"]


def tytles(covid19):
    tytles = (
    [item for item in list(covid19[0].keys()) if item not in ['ID', 'CountryCode', 'Slug', 'Date', 'Premium']])

    for item in tytles:
        if item == 'Country':
            print("{0:_^31s}".format(item), end=" ")
        else:
            print("{0:_>15s}".format(item), end=" ")
    else:
        print('')

    for item in covid19:
        for key in item:
            if key in tytles:
                if key == 'Country':
                    print("{0:<31}".format(item[key]), end="|")
                else:
                    print("{0:>15}".format(item[key]), end="|")

        else:
            print('')


def by_new_confirmed_key(covid19):
    return covid19['NewConfirmed']


while True:
    print('1. Show COVID19 information\n'
          '2. Sort by new confirmed\n'
          '3. Отримати детальну інформацію по назві країни ("Country")\n'
          '4. Show global information\n'
          '0. Выход')

    try:
        choice = int(input('Ведите значение 0-4: '))

        if choice == 0:
            print('до новых встреч')
            break
        elif choice == 1:
            print('------------- Информация по странам -----------------')
            tytles(covid19)
            input('Для возврата нажмите Enter')
        elif choice == 2:
            print('------------- Сортировка по новым сообщениям -----------------')
            covid19 = sorted(covid19, key=by_new_confirmed_key, reverse=True)
            tytles(covid19)
            input('Для возврата нажмите Enter')
        elif choice == 3:
            country = input('Введите страну латиницей(прим. Ukraine): ')
            print('------------- Подробная информация по стране -----------------')

            find = False
            for item_country in covid19:
                if country == item_country['Country']:
                    find = True
                    for key in item_country:
                        print(f'{key}: {item_country[key]}')

            if not find:
                print('**Ничего не найдено**')
            input('Для возврата нажмите Enter')
        elif choice == 4:
            print('------------- Global information -----------------')
            for key, val in enumerate(covid19_global):
                print(f'{val}: {covid19_global[val]}')
            input('Для возврата нажмите Enter')
        else:
            print('Введите значение от 0 до 4')
            continue
    except ValueError:
        print('Неверное значение. Введите значение от 0 до 4')