import requests
from datetime import datetime
import os
from time import sleep


success_file = open("files/access.log", "a")
error_file = open("files/error.log", "a")
# sleep(10)

try:
    TODAY = datetime.today().strftime("%d.%m.%Y")
    URL = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={TODAY}"

    response = requests.get(URL)
    PB = response.json()

    print(type(PB))
    print(type(PB['exchangeRate']))
    # for row in PB['exchangeRate']:
    #     print(row)

    success_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')} | {response.status_code} "
                       f"{response.reason} Operation success!\n")
except Exception as ex:
    error_file.write(f"| {os.getlogin()} | {datetime.today().strftime('%d.%m.%Y %H:%M:%S')} | "
                     f"Operation failed!\n")
finally:
    success_file.close()
    error_file.close()