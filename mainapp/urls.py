from django.urls import path
from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.index, name='home'),
    path('products/', mainapp_views.Products.as_view(), name='products'),
    path('category/<int:category_id>/', mainapp_views.ProductsByCategory.as_view(), name='category'),
]
