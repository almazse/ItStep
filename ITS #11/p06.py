import pprint

hitman = {
    'name': 'John Wick',
    'born': 1968,
    'guns': [
        {'mark': 'Beretta', 'bullets': 14},
        {'mark': 'Makarov', 'bullets': 8},
    ],
}

pprint.pprint(hitman)

# bullets_sum = 0
# for gun in hitman['guns']:
#     bullets_sum += gun['bullets']
# print(bullets_sum)

bullets_sum = sum(gun['bullets'] for gun in hitman['guns'])
print(bullets_sum)