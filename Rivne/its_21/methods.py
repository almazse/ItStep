import psycopg2
from settings import *
from connection import Connection
import datetime


class SuperAdmin(Connection):

    def __init__(self, login: str, password: str):
        self.login = login
        if isinstance(password, str):
            self.password = password
        else:
            raise TypeError('Incorrect data type')

    def add_admin(self, admin_data):
        table = 'users'
        result = self._postData(table, admin_data)
        return result


class Admin(Connection):

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def login_self(self):
        return self.login_check(self.login, self.password)

    def get_order_info(self, category='', selector='', ):
        """
        category must be one of the item from the list:
        ['city_name','date_of_order', 'product_name']

        date format for selector: 2020-6-12
        """
        if self.login_self():
            categories = ['city_name', 'date_of_order', 'product_name', 'status']
            table = ('orders o',)
            fields = ("""o.id, concat(e.first_name,' ', e.last_name) as "employee", c.city_name, o.date_of_order, 
            concat(c2.first_name,' ', c2.last_name) as "customer", p.product_name, o.price """,)
            if category and category in categories and selector != '':
                selector = selector if isinstance(selector, bool) == bool else str(selector)
                where = f"""where {category} = {selector}"""
            else:
                where = ''
            selector = f""" left JOIN employee e on e.id = o.employee_id 
                            left JOIN city c on c.id = o.city_id 
                            left JOIN customer c2 on c2.id = o.customer_id 
                            left JOIN product p on p.id = o.product_id {where}"""
            result = self.getData(table, fields, selector)
            fieldNames = ["id", "employee", "city_name", "date_of_order", "customer", "product_name", "price"]
            changeRes = []
            for item in result:
                cort = {}
                for index, element in enumerate(item):
                    cort[fieldNames[index]] = element
                changeRes.append(cort)
        else:
            changeRes = "Invalid login!"
        return changeRes

    def add_pr_category(self, data):
        table = 'product_category'
        result = self._postData(table, data)
        return result

    def edit_pr_category(self, data, selector):
        table = 'product_category'
        result = self.updateData(table, data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table, selector)
        return result


if __name__ == '__main__':

    admin_1_data = [{
        "first_name": "Billssss",
        "last_name": "Bobb",
        "date_of_bitrth": "02.05.1684",
        "phone": "+803254",
        "address": "Streee1",
        "password": "123",
        "email": "opa@mail.dog",
        "role": "admin",
        "discount": "20"
    }]
    # admin_1 = Admin('Bad','BOB')
    # admin_1.add_admin(admin_1_data)

    # admin_1 = SuperAdmin('Bad','BOB').add_admin(admin_1_data)

    admin_2 = Admin("opa@mail.dog", "123").login_self()
    print(admin_2)
