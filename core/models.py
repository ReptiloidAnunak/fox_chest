from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
    phone = models.CharField(max_length=26)
