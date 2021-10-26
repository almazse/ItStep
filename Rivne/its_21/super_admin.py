import psycopg2
from settings import *
from connection import Connection


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_admin(self, admin_data):
        table = 'users'
        result = self._postData(table, admin_data)
        return result
