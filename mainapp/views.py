from django.shortcuts import render
from mainapp.models import Category, Product
from django.views.generic import ListView
from django.conf import settings
from django.core.cache import cache


def get_links_category():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = Category.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return Category.objects.filter(is_active=True)


def get_products_by_category_ordered_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_by_category_ordered_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=pk, is_active=True,
                                              category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category_id=pk, is_active=True,
                                      category__is_active=True).select_related('category')


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


class Products(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Каталог',
            # 'categories': Category.objects.filter(is_active=True),
            'categories': get_links_category(),
        })
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
        # return Product.objects.filter(is_active=True, category__is_active=True)


class ProductsByCategory(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': Category.objects.get(pk=self.kwargs['category_id']),
            # 'categories': Category.objects.filter(is_active=True),
            'categories': get_links_category(),
        })
        return context

    def get_queryset(self):
        return get_products_by_category_ordered_by_price(self.kwargs['category_id'])
        # return Product.objects.filter(category_id=self.kwargs['category_id'], is_active=True,
        #                               category__is_active=True).select_related('category')
        # return Product.objects.filter(category_id=self.kwargs['category_id'], is_active=True,
        #                               category__is_active=True)
