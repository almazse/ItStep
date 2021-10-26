from connection import Connection
from datetime import datetime


class RegisteredCustomer(Connection):
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.first_name = ''
        self.last_name = ''
        self.city_id = ''
        self.id = ''
        self.get_login_customer_id()

    def login_self(self):
        if self.id:
            self.first_name = self.getData(('customer',), ('first_name',), f"where id = {self.id}")[0][0]
            self.last_name = self.getData(('customer',), ('last_name',), f"where id = {self.id}")[0][0]
            self.city_id = self.getData(('customer',), ('city_id',), f"where id = {self.id}")[0][0]
        return self.login_check(self.login, self.password, 'cus')

    def get_login_customer_id(self):
        if self.login_self():
            table = ('reg_base',)
            fields = ('customer_id',)
            selector = f"where login = '{self.login}'"
            result = self.getData(table, fields, selector)[0][0]
        else:
            result = "Invalid login!"
        self.id = result

    def edit_self_info(self, data, selector):
        if self.login_self():
            table = 'customer'
            result = self.updateData(table, data, selector)
        else:
            result = "Invalid login!"
        return result

    def create_order(self, products):
        if self.login_self():
            table = 'orders'
            data = []
            for item in products:
                order = {
                    "customer_id": self.id,
                    "city_id": self.city_id,
                    "date_of_order": datetime.today().strftime('%Y-%m-%d'),
                    "product_id": self.getData(('product',), ('id',), f"where product_name = '{item[0]}'")[0][0],
                    "price": self.getData(('product',), ('unit_price',), f"where product_name = '{item[0]}'")[0][0] * item[1]
                }
                data.append(order)
            result = self.postData(table, data)
            return result

    def delete_order(self, selector):
        if self.login_self():
            table = 'orders'
            selector = f"id = '{selector}'"
            result = self.deleteData(table, selector)
        else:
            result = "Invalid login!"
        return result

    def get_product_info(self, category='', selector='', ):
        """
        category must be one of the item from the list:
        ['city_name', 'category_name']
        """
        categories = ['city_name', 'category_name']
        table = ('product p',)
        fields = ("""p.id, p.product_name, p.unit_price, c.country_name, p2.category_name""",)
        if category and category in categories and selector:
            where = f"""where {category} = '{selector}'"""
        else:
            where = ''
        selector = f"""  inner JOIN country c on c.id = p.country_id 
                        inner JOIN product_category p2 on p2.id = p.product_category_id {where}"""
        result = self.getData(table, fields, selector)
        fieldNames = ["id", "product_name", "unit_price", "country_name", "category_name"]
        changeRes = []
        for item in result:
            cort = {}
            for index, element in enumerate(item):
                cort[fieldNames[index]] = element
            changeRes.append(cort)

        return changeRes
