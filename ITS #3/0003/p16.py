# NESTED LOOPS

# for i in range(1, 4):
#     print(f"i = {i}")
#
#     for j in 100, 200, 300, 400:
#         print(f"i = {i}, j = {j}")

for i in 1, 3, 5:
    for j in 2, 4, 6:
        print(f"{i} x {j} = {(i * j):>2}", end="  ")
    print()
