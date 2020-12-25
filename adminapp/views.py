from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from authapp.models import User
from mainapp.models import Category, Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminCreationForm, \
    ProductAdminCreationForm


class AccessClass:
    @method_decorator(user_passes_test(lambda user: user.is_superuser or user.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(AccessClass, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def index(request):
    return render(request, 'adminapp/index.html')


class AdminUserList(AccessClass, ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    context_object_name = 'users'


class AdminUserCreate(AccessClass, CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminRegisterForm


class AdminUserUpdate(AccessClass, UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm


class AdminUserDelete(AccessClass, DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminUserRecover(AccessClass, UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminCategoryList(AccessClass, ListView):
    model = Category
    template_name = 'adminapp/admin-categories-read.html'
    context_object_name = 'categories'


class AdminCategoryCreate(AccessClass, CreateView):
    model = Category
    template_name = 'adminapp/admin-categories-create.html'
    form_class = CategoryAdminCreationForm
    success_url = reverse_lazy('admin_staff:admin_categories')


class AdminCategoryUpdate(AccessClass, UpdateView):
    model = Category
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories')
    form_class = CategoryAdminCreationForm


class AdminProductList(AccessClass, ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    context_object_name = 'products'


class AdminProductCreate(AccessClass, CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProductAdminCreationForm
    success_url = reverse_lazy('admin_staff:admin_products')


class AdminProductUpdate(AccessClass, UpdateView):
    model = Product
    template_name = 'adminapp/admin-product-update-delete.html'
    form_class = ProductAdminCreationForm
    success_url = reverse_lazy('admin_staff:admin_products')
