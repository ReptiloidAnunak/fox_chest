from django.db import models

from .constants import WearSex, WearColor, BrandCountry, WearSize


class Brand(models.Model):
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField(max_length=50,
                            verbose_name='Название')
    country = models.CharField(max_length=20,
                               choices=BrandCountry.choices,
                               default=BrandCountry.NONE,
                               verbose_name='Страна')

    def __str__(self):
        return self.name


class Wear(models.Model):
    name = models.CharField(max_length=50,
                            null=True,
                            verbose_name='Название')
    size = models.CharField(max_length=2,
                            choices=WearSize.choices,
                            verbose_name='Размер')
    color = models.CharField(max_length=10,
                             choices=WearColor.choices,
                             default=WearColor.NONE,
                             verbose_name='Цвет')
    material = models.CharField(max_length=20,
                                null=True,
                                verbose_name='Материал')
    sex = models.CharField(max_length=6,
                           choices=WearSex.choices,
                           default=WearSex.UNISEX,
                           verbose_name='Пол')
    age = models.CharField(max_length=10,
                           null=True,
                           verbose_name='Возраст')

    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              verbose_name='Бренд')

    price = models.IntegerField(null=True,
                                verbose_name='Цена')
    description = models.CharField(max_length=200,
                                   null=True,
                                   verbose_name='Описание')
    image = models.ImageField(
        upload_to='wear/',
        blank=True,
        null=True,
        default='media/wear/img.png'
    )

    def __str__(self):
        return self.name


class TShort(Wear):
    class Meta:
        verbose_name = 'Майка'
        verbose_name_plural = 'Майки'


class Pants(Wear):
    class Meta:
        verbose_name = 'Штаны'
        verbose_name_plural = 'Штаны'


class Jacket(Wear):
    class Meta:
        verbose_name = 'Куртка'
        verbose_name_plural = 'Куртки'


class Bodysuit(Wear):
    class Meta:
        verbose_name = 'Боди'
        verbose_name_plural = 'Боди'