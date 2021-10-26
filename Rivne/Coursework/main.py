from methods import Admin, Editor, News
from datetime import datetime

if __name__ == '__main__':
    admin = Admin('admin', '123')

    # # add editor
    # new_editor_data = [{
    #     "login": "Editor2",
    #     "password": "222",
    #     "first_name": "Mark",
    #     "last_name": "Martin",
    #     "role": "editor"
    # }]
    # print(admin.add_editor(new_editor_data))

    # # edit editor
    # edit_editor_data = {
    #     'login': "Editor2",
    #     'password': "223",
    #     'first_name': "Jonathan",
    #     'last_name': "Mahoney"
    # }
    # edit = admin.edit_editor(edit_editor_data, "id = '3'")
    # print(edit)

    # # delete editor
    # delete = admin.delete_editor("id = '3'")
    # print(delete)

    editor = Editor('editor', '223')

    # # edit personal data
    # edit_personal_data = {
    #     'login': "Editor1",
    #     'password': "223",
    #     'first_name': "Jonathan",
    #     'last_name': "Mahoney"
    # }
    # print(editor.edit_personal_info(edit_personal_data))

    # # add article
    # article_data = [{
    #     "title": "Article Tennis",
    #     "category": "2",
    #     "image": "Racket.jpg",
    #     "text": "Martin",
    #     "author": editor.login_self(),
    #     "date_of_publish": datetime.now()
    # }]
    # print(editor.add_article(article_data))

    # edit article
    # edit_article_data = {
    #     "id": "1",
    #     "title": "Article Tennis",
    #     "category": "2",
    #     "image": "Racket.jpg",
    #     "text": "Lorem ipsum dolar",
    #     "author": editor.login_self(),
    #     "date_of_publish": datetime.now()
    # }
    # print(editor.edit_article(edit_article_data))

    # # delete article
    # delete = editor.delete_article(2)
    # print(delete)

    # # add category
    # category_data = [{
    #     "category_name": "Outer",
    #     "parent_id": 6
    # }]
    # print(editor.add_category(category_data))

    # # edit category
    # edit_category_data = {
    #     "id": "7",
    #     "category_name": "Other"
    # }
    # print(editor.edit_category(edit_category_data))

    # # delete category
    # delete = editor.delete_category(7)
    # print(delete)

    # # edit comment
    # edit_comment_data = {
    #     "id": "2",
    #     "name": "Irina"
    # }
    # print(editor.edit_comment(edit_comment_data))

    # # delete comment
    # delete = editor.delete_comment(3)
    # print(delete)

    def respprint(obj):
        if type(obj) == str:
            print(obj)
        else:
            keys = obj[0].keys()
            for item in keys:
                print("{0:20s}".format(item), end='\t')
            print()
            for item in obj:
                for index, element in enumerate(item):
                    print("{0:20s}".format(str(item[element])), end='\t')
                print()

    news = News()

    # # get category
    # respprint(news.get_category())

    # # get article
    # respprint(news.get_article())
    # respprint(news.get_article(category='date_of_publish', selector='2021-09-29'))
    # respprint(news.get_article(category='category_name', selector='Tenis'))

    # get comment
    # respprint(news.get_comment(1))

    # # add comment
    # print(news.add_comment(2, "Billy", "Lorem ipsum dolor"))

    # # subscribe
    # print(news.subscribe("Andy", "andy@email.com"))

    # # unsubscribe
    # print(news.unsubscribe("andy@email.com"))

    # print(news.get_exchange_rate())
