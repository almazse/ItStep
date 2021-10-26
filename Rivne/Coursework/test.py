import unittest
from datetime import datetime
from typing import List, Dict

from methods import Admin, Editor, News
from connection import Connection


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.admin = Admin("admin", "123")
        self.editor = Editor("editor", "223")
        self.news = News()
        self.connection = Connection()

    def test_is_instance_admin(self):
        self.assertIsInstance(self.admin, Admin)
        self.assertIsInstance(self.admin, Editor)
        self.assertIsInstance(self.admin, News)

    def test_is_instance_editor(self):
        self.assertIsInstance(self.editor, Editor)
        self.assertIsInstance(self.editor, News)

    def test_not_is_instance_editor(self):
        self.assertNotIsInstance(self.editor, Admin)

    def test_is_instance_news(self):
        self.assertIsInstance(self.news, News)

    def test_not_is_instance_news(self):
        self.assertNotIsInstance(self.news, Admin)
        self.assertNotIsInstance(self.news, Editor)

    def test_add_editor_admin(self):
        new_editor_data = [{
            "login": "TestEditor",
            "password": "test123",
            "first_name": "first_name",
            "last_name": "last_name",
            "role": "editor"
        }]
        self.assertEqual(self.admin.add_editor(new_editor_data), "Insert done!")

    def test_edit_editor_admin(self):
        edit_editor_data = {
            'login': "TestEditor",
            'password': "test123",
            'first_name': "edit_first_name",
            'last_name': "edit_last_name"
        }
        edit = self.admin.edit_editor(edit_editor_data, "login = 'TestEditor'")
        self.assertEqual(edit, "Update done!")

    def test_delete_editor_admin(self):
        delete = self.admin.delete_editor("login = 'TestEditor'")
        self.assertEqual(delete, "Item was deleted!")

    def test_edit_personal_data(self):
        edit_personal_data = {
            'login': "editor",
            'password': "223",
            'first_name': "personal_edit_first_name",
            'last_name': "personal_edit_last_name"
        }
        self.assertEqual(self.editor.edit_personal_info(edit_personal_data), "Update done!")
        self.editor.edit_personal_info({'first_name': 'Jonathan', 'last_name': 'Mahoney'})

    def test_add_article(self):
        article_data = [{
            "title": "Test Article",
            "category": "2",
            "image": "Test.jpg",
            "text": "Test text",
            "author": self.editor.login_self(),
            "date_of_publish": datetime.now()
        }]
        add_article = self.editor.add_article(article_data)
        table = ("article",)
        fields = ("id",)
        selector = "WHERE title = 'Test Article'"
        id_article = self.connection.getData(table, fields, selector)[0][0]
        self.editor.delete_article(id_article)
        self.assertEqual(add_article, "Insert done!")

    def test_edit_article(self):
        article_data = [{
            "title": "Test Article",
            "category": "2",
            "image": "Test.jpg",
            "text": "Test text",
            "author": self.editor.login_self(),
            "date_of_publish": datetime.now()
        }]
        self.editor.add_article(article_data)
        table = ("article",)
        fields = ("id",)
        selector = "WHERE title = 'Test Article'"
        id_article = self.connection.getData(table, fields, selector)[0][0]
        edit_article_data = {
            "id": id_article,
            "title": "Edit Test Article",
            "category": "2",
            "image": "Test.jpg",
            "text": "Edit Test text",
            "author": self.editor.login_self(),
            "date_of_publish": datetime.now()
        }

        edit_article = self.editor.edit_article(edit_article_data)
        self.editor.delete_article(id_article)
        self.assertEqual(edit_article, "Update done!")

    def test_delete_article(self):
        article_data = [{
            "title": "Test Article",
            "category": "2",
            "image": "Test.jpg",
            "text": "Test text",
            "author": self.editor.login_self(),
            "date_of_publish": datetime.now()
        }]
        self.editor.add_article(article_data)
        table = ("article",)
        fields = ("id",)
        selector = "WHERE title = 'Test Article'"
        id_article = self.connection.getData(table, fields, selector)[0][0]
        delete = self.editor.delete_article(id_article)
        self.assertEqual(delete, "Item was deleted!")

    def test_add_category(self):
        category_data = [{
            "category_name": "Test Category"
        }]
        add_category = self.editor.add_category(category_data)
        table = ("category",)
        fields = ("id",)
        selector = "WHERE category_name = 'Test Category'"
        id_category = self.connection.getData(table, fields, selector)[0][0]
        self.editor.delete_category(id_category)
        self.assertEqual(add_category, "Insert done!")

    def test_edit_category(self):
        category_data = [{
            "category_name": "Test Category"
        }]
        self.editor.add_category(category_data)
        table = ("category",)
        fields = ("id",)
        selector = "WHERE category_name = 'Test Category'"
        id_category = self.connection.getData(table, fields, selector)[0][0]

        edit_category_data = {
            "id": id_category,
            "category_name": "Edit Test Category"
        }
        edit_category = self.editor.edit_category(edit_category_data)
        self.editor.delete_category(id_category)
        self.assertEqual(edit_category, "Update done!")

    def test_delete_category(self):
        category_data = [{
            "category_name": "Test Category"
        }]
        self.editor.add_category(category_data)
        table = ("category",)
        fields = ("id",)
        selector = "WHERE category_name = 'Test Category'"
        id_category = self.connection.getData(table, fields, selector)[0][0]

        delete_category = self.editor.delete_category(id_category)
        self.assertEqual(delete_category, "Item was deleted!")

    def test_edit_comment(self):
        self.editor.add_comment(2, "Test Name", "Test Comment")
        table = ("comment",)
        fields = ("id",)
        selector = "WHERE name = 'Test Name'"
        id_comment = self.connection.getData(table, fields, selector)[0][0]
        edit_comment_data = {
            "id": id_comment,
            "name": "Edit Test Name",
            "text": "Edit Test Comment"
        }
        edit_comment = self.editor.edit_comment(edit_comment_data)
        self.editor.delete_comment(id_comment)
        self.assertEqual(edit_comment, "Update done!")

    def test_delete_comment(self):
        self.editor.add_comment(2, "Test Name", "Test Comment")

        table = ("comment",)
        fields = ("id",)
        selector = "WHERE name = 'Test Name'"
        id_comment = self.connection.getData(table, fields, selector)[0][0]

        delete_comment = self.editor.delete_comment(id_comment)
        self.assertEqual(delete_comment, "Item was deleted!")

    def test_get_article(self):
        get_article = self.news.get_article()
        self.assertIsInstance(get_article, List)

    def test_get_article_selector_date(self):
        get_article = self.news.get_article(category='date_of_publish', selector='2021-09-29')
        self.assertIsInstance(get_article, List)

    def test_get_article_selector_category(self):
        get_article = self.news.get_article(category='category_name', selector='Tenis')
        self.assertIsInstance(get_article, List)

    def test_get_category(self):
        get_category = self.news.get_category()
        self.assertIsInstance(get_category, List)

    def test_get_comment(self):
        get_comment = self.news.get_comment(1)
        self.assertIsInstance(get_comment, List)

    def test_add_comment(self):
        add_comment = self.news.add_comment(2, "Test Name", "Test Comment")

        table = ("comment",)
        fields = ("id",)
        selector = "WHERE name = 'Test Name'"
        id_comment = self.connection.getData(table, fields, selector)[0][0]

        self.editor.delete_comment(id_comment)
        self.assertEqual(add_comment, "Insert done!")

    def test_subscribe(self):
        subscribe = self.news.subscribe("TestName", "test@email.com")
        self.news.unsubscribe("test@email.com")
        self.assertEqual(subscribe, "You have successfully subscribed to the newsletter")

    def test_unsubscribe(self):
        self.news.subscribe("TestName", "test@email.com")
        unsubscribe = self.news.unsubscribe("test@email.com")
        self.assertEqual(unsubscribe, "You unsubscribed successfully")

    def test_admin_wrong_password(self):
        admin = Admin('AdminWrong', 'WrongPassword')
        self.assertFalse(admin.login_self())

    def test_admin_login(self):
        self.assertTrue(self.admin.login_self())

    def test_editor_wrong_password(self):
        editor = Editor('EditorWrong', 'WrongPassword')
        self.assertFalse(editor.login_self())

    def test_editor_login(self):
        self.assertTrue(self.editor.login_self())

    def test_get_exchange_rate(self):
        get_exchange_rate = self.news.get_exchange_rate()
        self.assertIsInstance(get_exchange_rate, Dict)


if __name__ == '__main__':
    unittest.main()
