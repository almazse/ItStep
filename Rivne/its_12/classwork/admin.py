import psycopg2
from settings import *
from connection import Connection


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_pr_category(self, data_cat):
        table = "product_category"
        result = self.postData(table, data_cat)
        return result

    def edit_pr_category(self, edit_data, selector):
        table = 'product_category'
        result = self.updateData(table, edit_data, selector)
        return result

    def delete_pr_category(self, selector):
        table = 'product_category'
        selector = f"category_name = '{selector}'"
        result = self.deleteData(table, selector)
        return result

    def register_self(self):
        pass

    def get_order_info(self, selector=''):
        table = ('orders',)
        fields = ('*',)
        result = self.getData(table, fields, selector)
        return result


if __name__ == '__main__':
    admin1 = Admin('Admin1', '1234')
    # orders1 = admin1.get_order_info()
    # print(orders1)

    # data = [{
    #     # 'id': 10,
    #     'category_name': "Beer"
    # }
    # ]
    # put = admin1.add_pr_category(data)
    # print(put)

    # data = {
    #     'category_name': "Water"
    # }
    #
    # admin1.edit_pr_category(data, "category_name = 'Beer'")

    # id = admin1.getNextId('product_category')
    # print(id)

    # print(admin1.delete_pr_category('Beer'))
