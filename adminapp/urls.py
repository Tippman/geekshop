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
]
