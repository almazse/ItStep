from tkinter import *
import json

FILENAME = 'school.json'

with open(FILENAME, 'r', encoding="utf-8") as f:
    data = json.load(f)


def insert_widget(txt, bg='yellow'):
    label = Label(text=txt, bg=bg)
    text.window_create(INSERT, window=label)


def insert_widget2(txt, bg='yellow'):
    label = Label(text=txt, bg=bg)
    text2.window_create(INSERT, window=label)


root = Tk()

text = Text(width=45, height=40)
text.grid(row=0, column=0)
text2 = Text(width=45, height=40)
text2.grid(row=0, column=1)

# Список классов
classes = set(list(pupil['class'] for pupil in data))

all_subjects = []
# Средние оценки каждого ученика
for pupil in data:
    marks = [mark[1] for mark in pupil['marks']]
    all_subjects.append([mark[0] for mark in pupil['marks']])
    pupil['mean'] = round(sum(marks) / len(marks), 2)

# Предметы
subjects = []
for i in all_subjects:
    for j in i:
        subjects.append(j)

# Оценки по предметам
mean_subject = dict()
for i in set(subjects):
    subjects_mean_marks = []
    subjects_pupils = []
    for pupils in data:
        for marks in pupils['marks']:
            if marks[0] == i:
                subjects_mean_marks.append(marks[1])
                subjects_pupils.append([pupils['name'], marks[1]])
    mean_subject[i] = {
        'subjects_mean': subjects_mean_marks,
        'subjects_pupils':  subjects_pupils,
    }

# формирование информации о классах
info_classes = dict()
for classes_i in classes:
    classes_mark = []
    classes_pupils = []
    for pupils in data:
        if pupils['class'] == classes_i:
            classes_mark.append(pupils['mean'])
            classes_pupils.append([pupils['name'], pupils['mean']])

    info_classes[classes_i] = {
        'mean_marks': round(sum(classes_mark) / len(classes_mark), 2),
        'classes_pupils': classes_pupils,
    }

# вывод информаци о классах
text.insert(INSERT, f'Информация по классам\n')
text.tag_add('title', 1.0, '1.end')
text.tag_config('title', justify=CENTER, font=("Arial", 12, 'bold'))
for classes_i in sorted(classes):
    insert_widget(f'Класс: {classes_i}')
    text.insert(INSERT, f"\n    Учеников в классе: {len(info_classes[classes_i]['classes_pupils'])}\n")
    text.insert(INSERT, f"    Средняя оценка класса: {info_classes[classes_i]['mean_marks']}\n")
    text.insert(INSERT, f"    3 лучших ученика:\n")
    for top3 in sorted(info_classes[classes_i]['classes_pupils'], key=lambda x: -x[1])[:3]:
        text.insert(INSERT, f"          {top3[0]} ({top3[1]})\n")

# вывод информации по предмета
text2.insert(INSERT, f'Средняя успеваемость по предметам\n')
text2.tag_add('title', 1.0, '1.end')
text2.tag_config('title', justify=CENTER, font=("Arial", 12, 'bold'))
for i in set(subjects):
    insert_widget2(f"{i} ({round(sum(mean_subject[i]['subjects_mean']) / len(mean_subject[i]['subjects_mean']), 2)})")
    text2.insert(INSERT, f"\n    3 лучших ученика по предмету:\n")
    for top3 in sorted(mean_subject[i]['subjects_pupils'], key=lambda x: -x[1])[:3]:
        text2.insert(INSERT, f"            {top3[0]} ({top3[1]})\n")

root.mainloop()
