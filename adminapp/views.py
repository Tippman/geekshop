from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import user_passes_test
from authapp.models import User
from mainapp.models import Category, Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminCreationForm, \
    ProductAdminCreationForm


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_users(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminRegisterForm()

    context = {'title': 'регистрация', 'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_users_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_users_recover(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryAdminCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
    else:
        form = CategoryAdminCreationForm()

    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_categories_update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryAdminCreationForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_categories'))
    else:
        form = CategoryAdminCreationForm(instance=category)
    context = {'form': form, 'category': category}
    return render(request, 'adminapp/admin-category-update-delete.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_products(request):
    context = {'products': Product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminCreationForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda user: user.is_superuser or user.is_staff)
def admin_product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_products'))
    else:
        form = ProductAdminCreationForm(instance=product)
    context = {'form': form, 'product': product}
    return render(request, 'adminapp/admin-product-update-delete.html', context)
