from admin import Admin
from pprint import *
from custom import respprint

admin = Admin('admin', '1111')
orders1 = admin.get_order_info(category='date_of_order', selector='2020-6-12')
respprint(orders1)


# if admin.login_self():
#     print(222)

