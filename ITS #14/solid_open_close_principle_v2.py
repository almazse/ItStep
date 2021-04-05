"""
WRONG!!!


class Discount:
    @staticmethod
    def give_discount(price, customer):
        if customer == 'fav':
            return price * 0.2
        elif customer == "vip":
            return price * 0.4

"""


class Discount:
    @staticmethod
    def give_discount(price):
        return price * 0.2


class VIPDiscount(Discount):
    @staticmethod
    def give_discount(price):
        return price * 0.4


class SuperVIPDiscount(Discount):
    @staticmethod
    def give_discount(price):
        return price * 0.8


