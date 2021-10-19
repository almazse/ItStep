from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.conf import settings


def homepage(request):
    return render(request, 'pages/index.html')


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    brand = None
    brands = Brand.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.objects.filter(category=category)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/store.html', {'category': category,
                                                'categories': categories,
                                                'products': products,
                                                'cart_product_form': cart_product_form})


def checkout(request):
    return render(request, 'pages/checkout.html')


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/product.html', {'product': product,
                                                  'cart_product_form': cart_product_form})
