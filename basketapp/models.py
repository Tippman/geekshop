from django.db import models
from authapp.models import User
from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#
#         super().delete()


class Basket(models.Model):
    # objects = BasketQuerySet.as_manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user.username} | Продукт {self.product.title}'

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by('product__category').select_related()

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    def get_user_baskets(self):
        return Basket.objects.filter(user=self.user).select_related()

    def get_total_sum_by_product(self):
        return self.product.price * self.quantity

    def get_total_sum(self):
        return sum(basket.get_total_sum_by_product() for basket in self.get_user_baskets())

    def get_total_quantity(self):
        return sum(basket.quantity for basket in self.get_user_baskets())

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()