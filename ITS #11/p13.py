import json
import pprint

FILENAME = 'school_.json'

with open(FILENAME, 'r', encoding="utf-8") as f:
    data = json.load(f)

for pupil in data:
    marks = [mark[1] for mark in pupil['marks']]
    pupil['mean'] = round(sum(marks) / len(marks), 2)

# pprint.pprint(data[0])

# print('TOP-3')
# for pupil in sorted(data, key=lambda x: -x['mean'])[:3]:
#     print(pupil['name'], pupil['class'], pupil['mean'])

mean_classes = dict()
classes = set(list(pupil['class'] for pupil in data))
for classes_i in classes:
    mean_classes[classes_i] = 0
    marks = []
    for pupils in data:
        if pupils['class'] == classes_i:
            marks.append(pupils['mean'])

    mean_classes[classes_i] = round(sum(marks) / len(marks), 2)

print(mean_classes)

