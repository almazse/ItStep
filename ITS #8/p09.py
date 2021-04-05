
# names = ["Billy", "Bobby", "Johnny"]
names = "Billy Bobby Johnny".split()
print(names)

letters = "A,B,C,D,E".split(",")
print(letters)

letters2 = tuple("ABCDE")
print(letters2)

s = " + ".join(names)
print(s, type(s))

s2 = "->".join(letters2)
print(s2)

a = [1, 2, 3]
# s3 = "+".join(a) # TypeError
