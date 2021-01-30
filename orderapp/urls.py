from django.urls import path
from orderapp import views as ordersapp_views

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp_views.OrderList.as_view(), name='orders'),
    path('create/', ordersapp_views.OrderCreate.as_view(), name='order_create'),
    path('update/<pk>/', ordersapp_views.OrderUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', ordersapp_views.OrderDelete.as_view(), name='order_delete'),
    path('detail/<pk>/', ordersapp_views.OrderDetail.as_view(), name='order_read'),
    path('forming/<pk>/', ordersapp_views.order_forming_complete, name='order_forming_complete'),
    path('get-price/', ordersapp_views.get_item_price, name='order_get_item_price'),
]
