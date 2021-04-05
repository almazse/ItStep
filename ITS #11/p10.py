distances = {
    (0, 1): 20,
    (0, 2): 30,
    (0, 3): 40,
    (1, 2): 50,
    (1, 3): 15,
    (2, 3): 10,
}

# for item in distances.items():
#     print(item)

start, finish = sorted([int(e) for e in input('введите маршрут: ').split()])
distance = distances.get((start, finish))
print(f'расстояние: {distance}')