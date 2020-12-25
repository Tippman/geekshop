from django.shortcuts import render
from mainapp.models import Category, Product
from django.views.generic import ListView


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
            'categories': Category.objects.filter(is_active=True),
        })
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True, category__is_active=True)


class ProductsByCategory(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': Category.objects.get(pk=self.kwargs['category_id']),
            'categories': Category.objects.filter(is_active=True),
        })
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id'], is_active=True, category__is_active=True)
