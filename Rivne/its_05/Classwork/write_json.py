import json

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
    'saleRateNB': '32.7722?',
    'purchaseRateNB': 32.7722,
    'saleRate': 32.95,
    'purchaseRate': 32.35
})

with open("files/data.json", 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True, ensure_ascii=True)

    outfile.close()

obj = {'saleRateNB': '32.7722?'}
rez = json.dumps(obj, ensure_ascii=False)
print(rez)
