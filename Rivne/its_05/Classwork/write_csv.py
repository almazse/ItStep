import csv

data = {'exchangeRate': []}
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'USD',
    'saleRateNB': 27.0275,
    'purchaseRateNB': 27.0275,
    'saleRate': 27.18,
    'purchaseRate': 26.75
})
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'PLZ',
    'saleRateNB': 7.2526,
    'purchaseRateNB': 7.2526,
    'saleRate': 7.35,
    'purchaseRate': 7.05
})
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'EUR',
    'saleRateNB': 32.7722,
    'purchaseRateNB': 32.7722,
    'saleRate': 32.95,
    'purchaseRate': 32.35
})

# item_list = ['baseCurrency', 'currency', 'saleRateNB', 'purchaseRateNB', 'saleRate', 'purchaseRate',
#              'Текстовое значение']

header = list(data['exchangeRate'][0].keys())

# file = open('files/data.csv', 'w', encoding='UTF8', newline='')
#
# writer = csv.writer(file)
#
# writer.writerow(header)
# writer.writerows([header, header])

with open('files/data.csv', 'w', encoding='UTF8', newline='') as file:

    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data['exchangeRate'])

    file.close()
