from django.shortcuts import render, HttpResponse
from mainapp.models import Category, Product


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Каталог',
        'categories': Category.objects.filter(is_active=True),
        'products': Product.objects.filter(is_active=True),
    }
    return render(request, 'mainapp/products.html', context)


# TODO - функция для обработки клика по категории
def products_by_category(request, category_id):
    context = {
        'title': Category.objects.get(id=category_id),
        'categories': Category.objects.filter(is_active=True),
        'products': Product.objects.filter(category=category_id)
    }
    return render(request, 'mainapp/products-by-category.html', context)
