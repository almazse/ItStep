from connection import Connection


class UnregisteredCustomer(Connection):

    def register_self(self, login, password):
        self.register(login, password, 'cus')

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
