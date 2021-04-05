import json

json_countries = ''

with open('countries.json', 'r') as f:
    json_countries_list_lines = f.readlines()
    json_countries += "".join(json_countries_list_lines)

# print(type(json_countries), json_countries[:10000])
# json_countries[0]['name']
countries_list = json.loads(json_countries)
print(type(countries_list), countries_list[:20])

ukraine = list(c for c in countries_list if c['name'] == 'Ukraine')
print(ukraine)
ukraine_json = json.dumps(ukraine[0])
with open('ukraine.json', 'w') as f:
    f.write(ukraine_json)