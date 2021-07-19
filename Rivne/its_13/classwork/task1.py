import pytest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def add_product(instance):
        discount = 0
        if instance.сount == 5:
            discount = 0.05
        elif instance.сount == 7:
            discount = 0.1
        elif instance.сount == 10:
            discount = 0.2
        elif instance.сount == 20:
            discount = 0.3
        elif instance.сount > 20:
            discount = 0.5

        return instance.price * instance.count - instance.price * instance.count * discount

class TestCart:
    def test_discount(self):
        self.cart

prod = Product('Apple', 10, 2)

cart = Cart

pay = cart.add_product(prod)
print(prod.count)
