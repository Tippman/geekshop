from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.admin_users, name='admin_users'),
    path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    path('users/edit/<int:user_id>/', adminapp.admin_users_edit, name='admin_users_edit'),
    path('users/remove/<int:user_id>/', adminapp.admin_users_remove, name='admin_users_remove'),
    path('users/recover/<int:user_id>/', adminapp.admin_users_recover, name='admin_users_recover'),
    path('categories/', adminapp.admin_categories, name='admin_categories'),
    path('categories/create/', adminapp.admin_categories_create, name='admin_categories_create'),
    path('categories/update/<int:category_id>/', adminapp.admin_categories_update, name='admin_categories_update'),
    path('products/', adminapp.admin_products, name='admin_products'),
    path('products/create/', adminapp.admin_products_create, name='admin_products_create'),
    path('products/update/<int:product_id>/', adminapp.admin_product_update, name='admin_product_update'),
]
