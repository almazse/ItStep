import re


def get_cortege_date(in_date):
    result = re.findall(r"([0-9]{4})[.\-/] ?([0-9]{1,2})[.\-/] ?([0-9]{1,2})", in_date)
    if result:
        date = (result[0][0], f"{result[0][1]:0>2}", f"{result[0][2]:0>2}")
    else:
        result = re.findall(r"([0-9]{1,2})[.\-/]([0-9]{1,2})[.\-/]([0-9]{4})", in_date)
        if result and int(result[0][1]) <= 12:
            date = (result[0][2], f"{result[0][1]:0>2}", f"{result[0][0]:0>2}")
        else:
            date = (result[0][2], f"{result[0][0]:0>2}", f"{result[0][1]:0>2}")
    return date


while True:
    try:
        choice = input('Ведите дату или exit для выхода: ')
        if choice == "exit":
            print('до новых встреч')
            break
        else:
            print(get_cortege_date(choice))
    except ValueError:
        print('Ведите дату или exit для выхода: ')

