import random
from faker import Faker
import json
fake = Faker('uk_UA')

FILENAME = 'school.json'

data = []
subjects = 'математика физика чтение физкультура ОБЖ пение рисование'.split()
classes = '1-А 1-Б 2-А 2-Б'.split()

for i in range(100):
    id = f'SCHOOL-{i+1}'
    name = fake.name()
    subjects_n = random.randint(4, 7)
    subjects_ = random.sample(subjects, subjects_n)
    # print(subjects_)
    # print(id, name)
    marks = [(s, random.randint(6, 12)) for s in subjects_]
    # print(marks)
    data.append({
        'id': id,
        'name': name,
        'marks': marks,
        'class': classes[i % len(classes)],
    })

with open(FILENAME, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)
    print('done.')
