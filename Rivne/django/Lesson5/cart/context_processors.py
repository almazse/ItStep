from .cart import Cart


def cart(request):
    widget_cart = Cart(request)
    widget_cart_count = widget_cart.__len__()

    return locals()