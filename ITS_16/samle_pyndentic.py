from dataclasses import dataclass
from pprint import pprint
from typing import List
from pydantic import BaseModel
from faker import Faker
'''
{
    "name": "Ukraine",
    "population": 52000000,
    "capital": {
        "name": "Kyiv",
        "population": 150000
    }
}
'''


class Capital(BaseModel):
    name: str
    population: int


class Country(BaseModel):
    name: str
    capital: Capital
    population: int


class Countries(BaseModel):
    countries: List[Country]


kyiv = Capital(name="Kyiv", population=1_500_000)
ukraine = Country(name='Ukraine', population=52_000_000, capital=kyiv)
pprint(ukraine)

print(ukraine.name)
print(ukraine.capital.name)

# print(type(ukraine.json()), ukraine.json())

fake = Faker()
fake.seed_locale('en_US', 0)
countries = []
for _ in range(1000):
    capital_name = f'{fake.name()}'
    capital_population = fake.unique.random_int()
    capital = Capital(name=capital_name, population=capital_population)
    country_name = f'{fake.name()}'
    country_population = fake.unique.random_int() + capital_population
    country = Country(name=country_name, capital=capital, population=country_population)
    countries.append(country)
countries_pydentic = Countries(countries=countries)
countries_json = countries_pydentic.json()

with open('countries_from_pydantic.json', 'w') as f:
    f.write(countries_json)

with open('countries.json', 'r') as f:
    countries_from_file = "".join(f.readlines())

countries_from_file = Countries.parse_file('countries_from_pydantic.json')
print(type(countries_from_file.countries[0].capital))

print(countries_from_file.countries[10].capital.name)

