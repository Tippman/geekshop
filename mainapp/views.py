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
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)


# TODO - функция для обработки клика по категории
def products_by_category(request):
    return HttpResponse('ok')
