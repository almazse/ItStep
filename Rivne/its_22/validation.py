import re
import unittest

from methods import SuperAdmin, Admin

# RegEX patterns
name_pattern = '/^([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)\-?([a-zA-Zа-щА-ЩЬьЮюЯяЇїІіЄєҐґ]+)$'
email_pattern = '^([a-zA-Z0-9-_\*\.]+)@([a-zA-Z0-9-]+)(\.[a-zA-Z0-9]+)+$'
password_pattern = '^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))$'
phone_pattern = '^\+\d{12}$'
date_pattern = '^([0-3]?[0-9])([\.|\-|\/])([0-1]?[0-9])([\.|\-|\/])(\d{4})$'
address_pattern = "^[A-Za-z0-9'\.\-\s\,]$"
role_pattern = '^(admin|super|user)$'
number_pattern = '^\d+\.?[0-9]*$'

USERS = {"id": [int, number_pattern], "first_name": [str, name_pattern], "last_name": [str, name_pattern],
         "date_of_bitrth": [str, date_pattern], "phone": [str, phone_pattern], "address": [str, address_pattern],
         "password": [str, password_pattern], "email": [str, email_pattern], "role": [str, role_pattern], "discount": [int, number_pattern]}

class Validate(unittest.TestCase):

    def validate(self, request, model, model_name):
        for key in request:
            self.assertIn(key, model, f'Field "{key}" is not in {model_name}. Incorrect field name!')
            self.assertIsInstance(request[key], model[key][0],
                                  f'Field "{key}" has invalid data type for {model_name} model, it must been {model[key][0]}. Incorrect field name!')
            self.assertRegex(request[key], model[key][1], f'Field "{key}" is not in {model_name}. Incorrect field name!')

if __name__ == '__main__':
    admin_1_data = [{
        "first_name": "Billssss",
        "last_name": "Bobb",
        "date_of_bitrth": "02-05-1684",
        "phone": "+803254",
        "address": "Streee1",
        "password": "123",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": 0
    }]

    Validate().validate(admin_1_data[0], USERS, "users")
    admin_1 = SuperAdmin('opa@mail.dog', '123D1d!')
    admin_1.add_admin(admin_1_data)

    for key in admin_1_data[0]:
        print(key)