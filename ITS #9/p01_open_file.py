# open() r - чтение w - запись a - запись в режиме добавления

# file = open("file.txt", "r", encoding="utf-8")
#
# content = file.read()
# print(content)
#
# file.close()

with open("open.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    # print(lines)
    # print(type(lines))
    for line in lines:
        print(line.strip())