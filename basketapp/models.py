from django.db import models
from authapp.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user.username} | Продукт {self.product.title}'

    def get_user_baskets(self):
        return Basket.objects.filter(user=self.user)

    def get_total_sum_by_product(self):
        return self.product.price * self.quantity

    def get_total_sum(self):
        return sum(basket.get_total_sum_by_product() for basket in self.get_user_baskets())

    def get_total_quantity(self):
        return sum(basket.quantity for basket in self.get_user_baskets())
