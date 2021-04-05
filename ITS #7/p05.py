# СРЕЗЫ СТРОК
# SLICES

s = "Madagascar"

n = 3
print(f"первые {n} символов:")
print(s[:n])

print(f"последние {n} символов:")
print(s[-n:])

print(f"начиная с {n}-го и до конца:")
print(s[n:])

n1 = 4
print(f"начиная с {n}-го {n1} символов:")
print(s[n:n + n1])

print("символы с четными индексами:")
print(s[::2])

print("символы с нечетными индексами:")
print(s[1::2])

print("символы в обратном порядке:")
print(s[::-1])


# ндекс 2-й буквы "a"

target = "a"
p1 = s.find(target)
print(p1)
p2 = s[p1 + 1:].find(target) + 1 + p1
print(p2)