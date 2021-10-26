from django.shortcuts import render, get_object_or_404
from .models import Product, Brand, Category
from cart.forms import CartAddProductForm
from django.conf import settings


def homepage(request):
    return render(request, 'pages/index.html')


def store(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    category_id_list = []
    for i in categories:
        if request.POST.get(f"category-{i.id}", False) == 'on':
            category_id_list.append(i.id)


    brand = None
    brands = Brand.objects.all()

    if category_id_list:
        products = Product.objects.filter(available=True, category__in=category_id_list)
    else:
        products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    return render(request, 'pages/store.html', {'category': category,
                                                'categories': categories,
                                                'products': products,
                                                'category_id_list': category_id_list})


def checkout(request):
    return render(request, 'pages/checkout.html')


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/product.html', {'product': product})
