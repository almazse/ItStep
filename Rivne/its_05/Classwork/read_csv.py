import csv

with open('files/data.csv', 'r', encoding='UTF8', newline='') as file:
    # file_reader = csv.reader(file, delimiter=' ', quotechar='|')
    # for row in file_reader:
    #     print(', '.join(row))

    file_reader = csv.DictReader(file)
    for row in file_reader:
        print(row)
        
    file.close()
