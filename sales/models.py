from django.db import models
from django.utils import timezone

from .constants import OrderStatus, DeliveryMethods
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
                                   through='OrderWearItem',
                                   verbose_name='Товары в корзине')

    status = models.CharField(max_length=20,
                              choices=OrderStatus.choices,
                              default=OrderStatus.CREATED,
                              verbose_name='Заказ')

    delivery_method = models.CharField(
        max_length=20,
        choices=DeliveryMethods.choices,
        default=DeliveryMethods.UNKNOWN,
        verbose_name='Способ доставки'
    )

    receiver = models.CharField(max_length=50,
                                verbose_name="Получатель",
                                null=True)

    phone_receiver = models.CharField(max_length=50,
                                      verbose_name="Телефон получателя",
                                      null=True)

    address = models.CharField(max_length=200,
                               verbose_name='Адрес',
                               null=True)

    total_price = models.IntegerField(default=0)

    final_price = models.IntegerField(default=0)

    discount = models.CharField(max_length=100,
                                verbose_name='Скидка',
                                default='Нет')

    def get_total_price(self):
        goods = self.goods.all()
        result = 0
        for obj in goods:
            result += obj.price
        return result

    def apply_discount_by_quantity(self):
        """3 вещи: -7%
        От 3-х: -10%"""
        discount = 0
        if len(list(self.goods.all())) == 3:
            self.discount = "3 вещи: -7%"
            discount = self.total_price * 0.07
        elif len(list(self.goods.all())) > 3:
            self.discount = "От 3-х вещи: -10%"
            discount = self.total_price * 0.1
        else:
            self.discount = "Нет"
            self.final_price = self.get_total_price()

        self.final_price -= discount
        self.save()
        return discount

    def create_order_msg(self):
        goods_lst = []
        goods = self.goods.all()
        print(goods)
        print(goods.all())
        count = 0
        self.total_price = self.get_total_price()
        self.save()
        for obj in goods:
            count += 1
            obj_str = obj.create_str_in_order(count)
            goods_lst.append(obj_str)
        goods_lst = "\n".join(goods_lst)
        self.apply_discount_by_quantity()
        result = (f"\n  ВАШ ЗАКАЗ\n\n"
                  f"Номер заказа:  {self.id}\n{self.created}"
                  f"\n{goods_lst}\n\n"
                  f"\nВсего: {self.total_price} руб.\n"
                  f"\nСкидка: {self.discount}\n"
                  f"\n\nВсего к оплате: {self.final_price} руб."
                  f"️⬇️ Выберите способ доставки ️⬇️")
        return result

    def create_final_order_msg(self):
        goods_lst = []
        goods = self.goods.all()
        count = 0
        self.total_price = self.get_total_price()
        self.save()
        for obj in goods:
            count += 1
            obj_str = (
                f"""
            {count}.  {obj.name} - {obj.brand} - {obj.size} - {obj.age} лет- {obj.price} р.
                            """)
            goods_lst.append(obj_str)
        goods_lst = "\n".join(goods_lst)
        result = (f"\n  ВАШ ЗАКАЗ\n"
                  f"\n\nНомер заказа:  {self.id}\n{self.created}"
                  f"\n\nФИО получателя: {self.receiver}"
                  f"\n\nТелефон получателя: {self.phone_receiver}"
                  f"\n\nАдрес доставки: {self.address}"
                  f"\n\nТовары: \n\n{goods_lst}\n"         
                  f"Всего: {self.total_price} руб.\n"
                  f"\nСкидка: {self.discount}"
                  f"\n\nВсего к оплате: {self.final_price} руб.")
        return result

    def __str__(self):
        return f"""{self.tg_user}: {self.created} - {self.status}"""


class Favorite(models.Model):
    tg_user = models.OneToOneField(TgUser,
                                   on_delete=models.CASCADE,
                                   verbose_name='Пользователь Телеграм')

    goods = models.ManyToManyField(Wear,
                                   blank=True,
                                   verbose_name='Товары')

    def __str__(self):
        return self.tg_user


class OrderWearItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    wear = models.ForeignKey(Wear, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def total_price(self):
        return self.wear.price * self.quantity