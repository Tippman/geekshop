from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html',context)


def products(request):
    context = {
        'title': 'Каталог',
        'products_list': [
            {'href': 'products_new', 'name': 'Новинки'},
            {'href': 'products_dress', 'name': 'Одежда'},
            {'href': 'products_shoes', 'name': 'Обувь'},
            {'href': 'products_accessories', 'name': 'Аксессуары'},
            {'href': 'products_presents', 'name': 'Подарки'},
        ],
    }
    return render(request, 'mainapp/products.html',context)
