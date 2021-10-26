import datetime


def respprint(obj):
    if type(obj) == str:
        print(obj)
    else:
        keys = obj[0].keys()
        for item in keys:
            print("{0:20s}".format(item), end='\t')
        print()
        for item in obj:
            for index, element in enumerate(item):
                print("{0:20s}".format(str(item[element])), end='\t')
