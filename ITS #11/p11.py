staff = [
    {'name': 'Иванова', 'salary': 1200},
    {'name': 'Петрова', 'salary': 1300},
    {'name': 'Сидорова', 'salary': 1700},
    {'name': 'Семенова', 'salary': 1400},
]

max_slary = max(person.get('salary') for person in staff)

richiest = [person for person in staff if person['salary'] == max_slary][0].get('name')

print('максимальная ЗП:', max_slary)
print('и её счастливая обладатель:', richiest)

staff.sort(key=lambda x: -x.get('salary'))
# for person in staff:
#     print(person)

richiest = staff[0]['name']
print('и её счастливая обладатель:', richiest)