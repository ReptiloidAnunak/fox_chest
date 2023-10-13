from django.db import models

from .constants import WearSex, WearColor, BrandCountry, WearSize


# ############################### Brand ##################################################

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


# ############################### Wear ##################################################

class Wear(models.Model):
    name = models.CharField(max_length=50,
                            null=True,
                            verbose_name='Название')
    size = models.CharField(max_length=3,
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
        default='media/wear/майка.png',
        verbose_name='Фотография'
    )

    quantity = models.PositiveIntegerField(null=True,
                                   default=0,
                                   verbose_name='Количество')

    def add_to_cart(self):
        pass

    def create_str_in_order(self, number):
        # - {amount_bought}
        str_in_order = f"""
        {number}.  {self.name} - {self.brand} - {self.size} - {self.age} лет - {self.price} р. 
                        """
        return str_in_order


    def __str__(self):
        return self.name


class TShort(Wear):
    class Meta:
        verbose_name = 'Майка'
        verbose_name_plural = 'Майки'


class Pants(Wear):
    class Meta:
        verbose_name = 'Штаны, джинсы'
        verbose_name_plural = 'Штаны, джинсы'


class Jacket(Wear):
    class Meta:
        verbose_name = 'Верхняя одежда'
        verbose_name_plural = 'Верхняя одежда'


class Bodysuit(Wear):
    class Meta:
        verbose_name = 'Боди, слип'
        verbose_name_plural = 'Боди, слипы'


class Overall(Wear):
    class Meta:
        verbose_name = 'Комбинезон'
        verbose_name_plural = 'Комбинезоны'


class ClothingSet(Wear):
    class Meta:
        verbose_name = 'Костюм/комплект'
        verbose_name_plural = 'Костюмы/комплекты'


class Robe(Wear):
    class Meta:
        verbose_name = 'Платье'
        verbose_name_plural = 'Платья'

    # sex = WearSex.FEMALE


class LongSleeve(Wear):
    class Meta:
        verbose_name = 'Лонгслив'
        verbose_name_plural = 'Лонгсливы'


class Underwear(Wear):
    class Meta:
        verbose_name = 'Нижнее белье'
        verbose_name_plural = 'Нижнее белье'


class SocksTights(Wear):
    class Meta:
        verbose_name = 'Носки/колготки'
        verbose_name_plural = 'Носки/колготки'


class Sweatshirt(Wear):
    class Meta:
        verbose_name = 'Cвитшот'
        verbose_name_plural = 'Cвитшоты'


# ############################### Doll ##################################################


class Doll(models.Model):
    class Meta:
        verbose_name = 'Кукла'
        verbose_name_plural = 'Куклы'

    name = models.CharField(max_length=50,
                            null=True,
                            verbose_name='Название')
    material = models.CharField(max_length=20,
                                null=True,
                                verbose_name='Материал')

    number_of_figures = models.IntegerField(verbose_name='Количество фигур',
                                            default=1)

    price = models.IntegerField(null=True,
                                verbose_name='Цена')

    description = models.CharField(max_length=200,
                                   null=True,
                                   verbose_name='Описание')
    image = models.ImageField(
        upload_to='dolls/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )


class Angel(Doll):
    class Meta:
        verbose_name = 'Ангел'
        verbose_name_plural = 'Ангелы'


class Family(Doll):
    class Meta:
        verbose_name = 'Семья кукол'
        verbose_name_plural = 'Семьи кукол'

