import pprint
import json

hitman = {
    'name': 'John Wick',
    'born': 1968,
    'guns': [
        {'mark': 'Beretta', 'type': 'pistol', 'bullets': 14},
        {'mark': 'AK-74', 'type': 'assault rifle', 'bullets': 30},
        {'mark': 'Makarov', 'type': 'pistol','bullets': 8},
        {'mark': 'Uzi', 'type': 'assault rifle', 'bullets': 22},
        {'mark': 'Maxim', 'type': 'machine gun', 'bullets': 120},
    ],
}

# pprint.pprint(hitman)

# список типов оружия
# gun_type = set(list(gun['type'] for gun in hitman['guns']))
# print(gun_type)

gun_types = []
for t in [gun['type'] for gun in hitman['guns']]:
    if t not in gun_types:
        gun_types.append(t)

print(gun_types)

gun_types_as_dict = dict()
for gun_type in gun_types:
    # s = 0
    # for gun in hitman['guns']:
    #     if gun['type'] == gun_type:
    #         s += gun['bullets']
    s = sum(gun['bullets'] for gun in hitman['guns'] if gun['type'] == gun_type)
    gun_types_as_dict[gun_type] = s

# pprint.pprint(gun_types_as_dict)

for t, b in sorted(gun_types_as_dict.items(), key=lambda x: -x[1]):
    print(t, b)

# JSON STR
hitman_json_string = json.dumps(hitman, indent=3)
print(hitman_json_string)
print(type(hitman_json_string))

hitman_unchained = json.loads(hitman_json_string)
print(hitman_unchained['name'])
print(type(hitman_unchained))

# JSON FILE
with open('hitman.json', 'w') as f:
    json.dump(hitman_unchained, f, indent=3)
    print('hitman to file done.')

with open('hitman.json', 'r') as f1:
    hitman_unchained_2 = json.load(f1)
    print('hitman from file done.')
    print(type(hitman_unchained_2))
    for k in hitman_unchained_2.keys():
        print(k)