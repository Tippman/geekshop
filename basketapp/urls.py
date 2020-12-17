from django.urls import path
import basketapp.views as basketapp_views

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:product_id>/', basketapp_views.basket_add, name='basket_add'),
    path('remove/<int:product_id>/', basketapp_views.basket_remove, name='basket_remove'),
    path('edit/<int:basket_id>/<int:quantity>', basketapp_views.basket_edit, name='basket_edit'),
]
