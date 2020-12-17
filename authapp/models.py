from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='authapp/users_avatars', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    def __str__(self):
        return self.username
