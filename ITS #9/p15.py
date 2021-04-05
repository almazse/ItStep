a = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

for row in a:
    print(row)

moves_X = [6, 0, 3, 5]

for c1, c2, c3 in a:
    print(c1, c2, c3)
    if all(c in moves_X for c in (c1, c2, c3)):
        print("WIN")
