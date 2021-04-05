# все ли эл-ты четные?

a = [2, 4, 12, 24, 120]

all_even = all(e % 2 == 0 for e in a)
print("YES" if all_even else "NO")

# хотябы один четный элемент?
b = [1, 7, 5, 99, 3]

any_even = any(e % 2 == 0 for e in b)
print("YES" if any_even else "NO")