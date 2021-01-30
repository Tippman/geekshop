from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Наименование категории')
    description = models.TextField(blank=True, verbose_name='описание категории')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Статус', default=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('mainapp:category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=150, unique=True, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    short_description = models.CharField(max_length=100, blank=True, verbose_name='Короткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    image = models.ImageField(upload_to='mainapp/products_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Статус товара')

    def __str__(self):
        return f'{self.title} ({self.category.title})'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category', 'title')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
