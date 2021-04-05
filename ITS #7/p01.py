# СТРОКИ

s = "hello"

print(s, type(s))
print(len(s))

print(s[0])
print(s[-1])
# print(s[99]) IndexError: string index out of range
# s[0] = "H" TypeError: 'str' object does not support item assignment

print()
for i in range(len(s)):
    print(i, s[i])

print()
for i, e in enumerate(s):
    print(i, e)

print(s.upper())
print(s.lower())
print(s.capitalize())
print('hello my dear friend'.title())
print('hello my dear friend'.upper())