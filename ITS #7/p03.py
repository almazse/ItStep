line = "abracadabra"

for part in "a", "abr", "x", "bra", "zz":
    if part in line:
        print(f"\"{part}\" содержится в \"{line}\"")
    else:
        print(f"\"{part}\" не содержится в \"{line}\"")

    if line.startswith(part):
        print(f"\"{line}\" начинается с \"{part}\"")
    else:
        print(f"\"{line}\" не начинается с \"{part}\"")

    if line.endswith(part):
        print(f"\"{line}\" заканчивается с \"{part}\"")
    else:
        print(f"\"{line}\" не заканчивается с \"{part}\"")
