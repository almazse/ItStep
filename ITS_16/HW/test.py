import json


countries = [
    {
        1: {
            'name': 'Tom',
            'age': 3
        },
        2: {
            'name': 'Jim',
            'age': 5
        },
        3: {
            'name': 'Ojjy',
            'age': 8
        },
        4: {
            'name': 'Jilly',
            'age': 8
        },
        5: {
            'name': 'Andy',
            'age': 8
        }
    }
]

print(type(countries[0]), countries[0])
dumped_countries = json.dumps(countries)
print(dumped_countries)