boy = {
    "name": "Billy",
    "age": 13,
    "marks": [11, 8, 10],
}

boy["gender"] = "M"
boy["age"] += 1
boy["marks"].append(12)

print(type(boy))
print(boy)
print(boy["name"])
print(boy["marks"])
print()

for key in sorted(boy.keys()):
    print(key, boy[key])

print()

# for v in boy.values():
#     print(v)

for k, v in boy.items():
    print(f"{k} -> {v}")