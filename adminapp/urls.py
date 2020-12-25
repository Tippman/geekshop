from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.AdminUserList.as_view(), name='admin_users'),
    path('users/create/', adminapp.AdminUserCreate.as_view(), name='admin_users_create'),
    path('users/edit/<int:pk>/', adminapp.AdminUserUpdate.as_view(), name='admin_users_edit'),
    path('users/remove/<int:pk>/', adminapp.AdminUserDelete.as_view(), name='admin_users_remove'),
    path('users/recover/<int:pk>/', adminapp.AdminUserRecover.as_view(), name='admin_users_recover'),
    path('categories/', adminapp.AdminCategoryList.as_view(), name='admin_categories'),
    path('categories/create/', adminapp.AdminCategoryCreate.as_view(), name='admin_categories_create'),
    path('categories/update/<int:pk>/', adminapp.AdminCategoryUpdate.as_view(), name='admin_categories_update'),
    path('products/', adminapp.AdminProductList.as_view(), name='admin_products'),
    path('products/create/', adminapp.AdminProductCreate.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>/', adminapp.AdminProductUpdate.as_view(), name='admin_product_update'),
]
