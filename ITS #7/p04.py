line = "abracadabra"

for c in "abcdef":
    if c in line:
        p = line.find(c)
        print(f"\"{c}\" на позиции {p}")
        n = line.count(c)
        print(f"кол-во вхождений: {n}")
    else:
        print(f"\"{c}\" не найдена")

print(line.find("z"))

print("-----------------")

# ндекс 2-й буквы "a"

counter = 0
target = "a"

for i, c in enumerate(line):
    if c == target:
        counter += 1
        # print(i)
        if counter == 2:
            second_posotion = i
            break

print(second_posotion)
