from connection import Connection
import requests

message = {
    "wrong_login": "Not enough privileges or wrong login or password!",
}


class News(Connection):

    def get_category(self):
        table = ('category c',)
        fields = ("""c.id, cat.category_name, c.category_name""",)
        selector = f""" left JOIN category cat on c.parent_id = cat.id """
        result = self.getData(table, fields, selector)
        fieldNames = ["id", "parent category", "category name"]
        changeRes = []
        for item in result:
            cort = {}
            for index, element in enumerate(item):
                cort[fieldNames[index]] = element
            changeRes.append(cort)
        return changeRes

    def get_article(self, category='', selector='', ):
        """
        category must be one of the item from the list:
        ['date_of_publish', 'category_name']

        date format for selector: 2020-6-12
        """
        categories = ['date_of_publish', 'category_name', 'author']
        table = ('article a',)
        fields = ("""a.id, a.date_of_publish, c.category_name, concat(u.first_name,' ', u.last_name), a.text""",)
        if category and category in categories and selector != '':
            selector = selector if isinstance(selector, bool) == bool else str(selector)
            where = f""" where {category} = '{selector}'"""
        else:
            where = ''
        selector = f""" left JOIN category c on c.id = a.category 
                        left JOIN users u on u.id = a.author{where}"""
        result = self.getData(table, fields, selector)
        fieldNames = ["id", "date of publish", "category name", "author", "text"]
        changeRes = []
        for item in result:
            cort = {}
            for index, element in enumerate(item):
                cort[fieldNames[index]] = element
            changeRes.append(cort)

        return changeRes

    def get_comment(self, id_article):
        table = ('comment c',)
        fields = ("""c.id, c.name, c.text""",)
        selector = f"WHERE article_id='{id_article}'"
        result = self.getData(table, fields, selector)
        fieldNames = ["id", "name", "text"]
        changeRes = []
        for item in result:
            cort = {}
            for index, element in enumerate(item):
                cort[fieldNames[index]] = element
            changeRes.append(cort)
        return changeRes

    def add_comment(self, id_article, name, text):
        table = 'comment'
        comment_data = [{
            "article_id": id_article,
            "name": name,
            "text": text
        }]
        result = self.postData(table, comment_data)
        return result

    def subscribe(self, name, email):
        table = 'subscriber'
        comment_data = [{
            "name": name,
            "email": email
        }]
        result = self.postData(table, comment_data)
        if result == "Insert done!":
            return "You have successfully subscribed to the newsletter"

    def unsubscribe(self, email):
        table = 'subscriber'
        result = self.deleteData(table, f"email = '{email}'")
        if result == "Item was deleted!":
            return "You unsubscribed successfully"

    @staticmethod
    def get_exchange_rate():
        URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        exchange_rate = {}
        for i in requests.get(URL).json():
            if i['cc'] == "USD" or i['cc'] == "RUB" or i['cc'] == "EUR":
                exchange_rate[i['cc']] = i['rate']
        return exchange_rate


class Editor(News):

    def __init__(self, login: str, password: str):
        self.login = login
        if isinstance(password, str):
            self.password = password
        else:
            raise TypeError('Incorrect data type')

    def login_self(self):
        return self.loginCheck(self.login, self.password, 'editor')

    def edit_personal_info(self, edit_personal_data):
        if self.login_self():
            table = 'users'
            result = self.updateData(table, edit_personal_data, f"id = '{self.login_self()}'")
            return result
        else:
            return message['wrong_login']

    def add_article(self, article_data):
        if self.login_self():
            table = 'article'
            result = self.postData(table, article_data)
            return result
        else:
            return message['wrong_login']

    def edit_article(self, edit_article_data):
        if self.login_self():
            table = 'article'
            result = self.updateData(table, edit_article_data, f"id = {int(edit_article_data['id'])}")
            return result
        else:
            return message['wrong_login']

    def delete_article(self, id_article):
        if self.login_self():
            table = 'article'
            result = self.deleteData(table, f"id = {id_article}")
            return result
        else:
            return message['wrong_login']

    def add_category(self, category_data):
        if self.login_self():
            table = 'category'
            result = self.postData(table, category_data)
            return result
        else:
            return message['wrong_login']

    def edit_category(self, edit_category_data):
        if self.login_self():
            table = 'category'
            result = self.updateData(table, edit_category_data, f"id = {int(edit_category_data['id'])}")
            return result
        else:
            return message['wrong_login']

    def delete_category(self, id_category):
        if self.login_self():
            table = 'category'
            result = self.deleteData(table, f"id = '{id_category}'")
            return result
        else:
            return message['wrong_login']

    def edit_comment(self, edit_comment_data):
        if self.login_self():
            table = 'comment'
            result = self.updateData(table, edit_comment_data, f"id = {int(edit_comment_data['id'])}")
            return result
        else:
            return message['wrong_login']

    def delete_comment(self, id_comment):
        if self.login_self():
            table = 'comment'
            result = self.deleteData(table, f"id = '{id_comment}'")
            return result
        else:
            return message['wrong_login']


class Admin(Editor):

    def __init__(self, login: str, password: str):
        super().__init__(login, password)
        self.login = login
        if isinstance(password, str):
            self.password = password
        else:
            raise TypeError('Incorrect data type')

    def login_self(self):
        return self.loginCheck(self.login, self.password, 'admin')

    def add_editor(self, editor_data):
        if self.login_self():
            table = 'users'
            users = self.getData((table,), ("login",), f"WHERE login='{editor_data[0]['login']}'")
            if not users:
                result = self.postData(table, editor_data)
            else:
                result = "This login already exists!"
            return result
        else:
            return "Not enough privileges or wrong login or password!"

    def edit_editor(self, editor_data, selector):
        if self.login_self():
            table = 'users'
            result = self.updateData(table, editor_data, selector)
            return result
        else:
            return "Not enough privileges or wrong login or password!"

    def delete_editor(self, selector):
        if self.login_self():
            table = 'users'
            result = self.deleteData(table, selector)
            return result
        else:
            return "Not enough privileges or wrong login or password!"
