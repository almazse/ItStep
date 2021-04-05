"""

{
    "name": "Oleh",
    "birthdate": {
        "time": 22,
        "month": 08,
        "year": 1991,
        "day": 25
    },
    "is_married": false,
    "parents": ["mama", "papa"]
}

"""
import json

countries = [
    {
        'Ukraine': {
            'population': 52_000_000,
            'capital': 'Kyiv',
            'states': [
                'Zaporizhizka oblast',
                'Kyivska oblast'
            ]
        },
        'Latvia': {
            'population': 32_000_000,
            'capital': 'Riga',
            'states': [
                'Rigska oblast',
                'Other oblast'
            ]
        },
    }
]

dumped_countries = json.dumps(countries)
print(type(countries), countries)
print('----------------------------------')
print(type(dumped_countries), dumped_countries)
print('----------------------------------')
loaded_countries = json.loads(dumped_countries)
print(type(loaded_countries), loaded_countries)


