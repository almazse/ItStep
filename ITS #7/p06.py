# s1 = "boo"
# s2 = "foo"
#
# print(s1 * 3 + s2 * 3)
# print((s2 + s1) * 3)

# "Воробей Джек" -> "Джек Воробей"

# line = "Воробей Джек"
line = input("Ввод данных: ")
print(line)

p = line.find(" ")
first = line[:p]
second = line[p+1:]
line2 = second + " " + first
print(line2)
line3 = f"{second} {first}"
print(line3)

one, two = line.split()
print(f"{two} {one}")
