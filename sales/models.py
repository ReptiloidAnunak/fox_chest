from django.db import models
from django.utils import timezone

from .constants import OrderStatus
from bot.models import TgUser
from store.models import Wear
from core.models import User


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Абстрактный класс - у него не будет таблицы

    created = models.DateTimeField(verbose_name="Дата создания")
    updated = models.DateTimeField(verbose_name="Дата последнего обновления")

    def save(self, *args, **kwargs) -> None:
        if not self.id:  # Когда модель только создается – у нее нет id
            self.created = timezone.now()
        self.updated = timezone.now()  # Каждый раз, когда вызывается save, проставляем свежую дату обновления
        return super().save(*args, **kwargs)


class Order(DatesModelMixin):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    tg_user = models.ForeignKey(TgUser,
                                on_delete=models.CASCADE,
                                verbose_name='Пользователь Телеграм')
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 verbose_name='Исполнитель',
                                 blank=True,
                                 null=True
                                 )

    goods = models.ManyToManyField(Wear,
                                   blank=True,
                                   verbose_name='Товары')

    status = models.CharField(max_length=20,
                              choices=OrderStatus.choices,
                              default=OrderStatus.CREATED,
                              verbose_name='Заказ')

    def __str__(self):
        return f"""{self.tg_user}: {self.created} - {self.status}"""
