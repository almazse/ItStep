"""

Дата класс хранит названия
музыкальных групп(исполнителей) и альбомов

"""

from pydantic import BaseModel
from typing import List
from faker import Faker


class Album(BaseModel):
    name: str
    year: int


class Band(BaseModel):
    name: str
    albums: List[Album]


fake = Faker()
fake.seed_locale('en_US', 0)
album_list = []
for _ in range(250):
    for _ in range(1, 5):
        album_name = f'{fake.name()}'
        album_year = fake.unique.random_int()
        album = Album(name=album_name, year=album_year)
        album_list.append(album)
    band_name = f'{fake.name()}'
    band = Band(name=band_name, albums=album_list)

band_json = band.json()

with open('band_from_pydantic.json', 'w') as f:
    f.write(band_json)

with open('band_from_pydantic.json', 'r') as f:
    band_from_file = "".join(f.readlines())

band_from_file = Band.parse_file('band_from_pydantic.json')
print(type(band_from_file))

print(band_from_file.albums[0].name)