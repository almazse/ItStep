import pprint

countries = 'USA;Great Britain;China'.split(';')
print(countries)

capitals = 'Washington London Beijing'.split()
print(capitals)

data = {}
# 1
# for i in range(len(countries)):
#     c1 = countries[i]
#     c2 = capitals[i]
#     data[c1] = c2

# 2
# for c1, c2 in zip(countries, capitals):
#     data[c1] = c2


# 3
# data = dict(zip(countries, capitals))

# 4
data = {c1:c2 for c1, c2 in zip(countries, capitals)}

print(data)

# for country in 'USA', 'Zimbabwe', 'China':
#     if country in data:
#         capital = data[country]
#         print(f'{capital} is the capital of {country}')
#     else:
#         print(f'I don\'t know the capital of {country}')

# for country in 'USA', 'Monaco', 'China':
#     try:
#         capital = data[country]
#     except KeyError:
#         capital = 'Запорожье'
#     finally:
#         print(f'{capital} is the capital of {country}')

for country in 'USA', 'Monaco', 'China':
    capital = data.get(country, 'Zaporozhye')
    print(f'{capital} is the capital of {country}')

# data.get('USA') = 'New York' # SyntaxError
