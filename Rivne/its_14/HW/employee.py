from connection import Connection


class Employee(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def login_self(self):
        return self.login_check(self.login, self.password, 'emp')

    def get_login_employee_id(self):
        if self.login_self():
            table = ('reg_base',)
            fields = ('employee_id',)
            selector = f"where login = '{self.login}'"
            result = self.getData(table, fields, selector)[0][0]
        else:
            result = "Invalid login!"
        return result

    def edit_self_info(self, data, selector):
        if self.login_self():
            table = 'employee'
            result = self.updateData(table, data, selector)
        else:
            result = "Invalid login!"
        return result

    def change_order_status(self, data, selector):
        if self.login_self():
            table = 'orders'
            result = self.updateData(table, data, selector)
        else:
            result = "Invalid login!"
        return result
