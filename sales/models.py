from django.db import models
from django.utils import timezone

from sales.constants import OrderStatus, DeliveryMethods, OFFICE_ADDRESS

from bot.models import TgUser
from store.models import Wear, Doll
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
        verbose_name = "Заказ одежды"
        verbose_name_plural = "Заказы одежды"

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
    total_units_quantity = models.PositiveIntegerField(default=0)


    def get_order_price(self):
        order_items = OrderWearItem.objects.filter(order=self)
        result = 0
        for item in order_items:
            result += int(item.get_total_price())
        self.total_price = result
        self.save()

    def apply_discount_by_quantity(self):
        """3 вещи: -7%
        От 3-х: -10%"""
        discount = 0
        if self.total_units_quantity == 3:
            self.discount = "3 вещи: -7%"
            discount = self.total_price * 0.07

        elif int(self.total_units_quantity) > 3:
            self.discount = "От 3-х вещи: -10%"
            discount = self.total_price * 0.1
        else:
            self.discount = "Нет"
        self.final_price = self.total_price - discount
        self.save()
        return discount


    def create_order_msg(self, item_cart_class):
        print("create_order_msg")
        goods_lst = []
        goods = self.goods.all()
        count = 0

        for obj in goods:
            item_in_cart = item_cart_class.objects.filter(order=self,
                                                          wear=obj).first()
            count += 1
            obj_str = obj.create_str_in_order(number=count,
                                              item_in_cart=item_in_cart)
            goods_lst.append(obj_str)

        goods_lst = "\n".join(goods_lst)

        self.get_order_price()
        self.apply_discount_by_quantity()

        created = self.created.strftime("%Y-%m-%d %H:%M")
        result = (f"\n  ВАШ ЗАКАЗ\n\n"
                  f"Номер заказа:  {self.id}"
                  f"\nВремя оформления: {created}"
                  f"\n\nФИО получателя: {self.receiver}"
                  f"\n\nТелефон получателя: {self.phone_receiver}"
                  f"\n\nСпособ доставки: {self.delivery_method}"
                  f"\n\nАдрес доставки: {self.address}"
                  f"\n{goods_lst}\n\n"
                  f"\nВсего: {self.total_price} руб.\n"
                  f"\nСкидка: {self.discount}\n"
                  f"\n\nВсего к оплате: {self.final_price} руб.")
        return result

    def create_final_order_msg(self):
        goods_lst = []
        goods = self.goods.all()
        count = 0
        for obj in goods:
            count += 1
            order_item = OrderWearItem.objects.filter(order=self,
                                                       wear=obj).first()

            obj_str = obj.create_str_in_order(number=count,
                                              item_in_cart=order_item)
            goods_lst.append(obj_str)
        goods_lst = "\n".join(goods_lst)
        created = self.created.strftime("%Y-%m-%d %H:%M")

        self.get_order_price()
        self.apply_discount_by_quantity()

        result = (f"\n  ВАШ ЗАКАЗ\n"
                  f"\n\nНомер заказа:  {self.id}"
                  f"\nВремя оформления: {created}"
                  f"\n\nФИО получателя: {self.receiver}"
                  f"\n\nТелефон получателя: {self.phone_receiver}"
                  f"\n\nСпособ доставки: {self.delivery_method}"
                  f"\n\nАдрес доставки: {self.address}"
                  f"\n\nТовары: \n\n{goods_lst}\n"         
                  f"Всего: {self.total_price} руб.\n"
                  f"\nСкидка: {self.discount}"
                  f"\n\nВсего к оплате: {self.final_price} руб.")
        return result

    def create_order_msg_pickup(self):
        goods_lst = []
        goods = self.goods.all()
        count = 0
        for obj in goods:
            count += 1
            order_item = OrderWearItem.objects.filter(order=self,
                                                      wear=obj).first()

            obj_str = obj.create_str_in_order(number=count,
                                              item_in_cart=order_item)
            goods_lst.append(obj_str)
        goods_lst = "\n".join(goods_lst)
        created = self.created.strftime("%Y-%m-%d %H:%M")

        self.get_order_price()
        self.apply_discount_by_quantity()

        result = (f'Вы получите товар по адресу:\n{OFFICE_ADDRESS}.\n'
                  f"\n  ВАШ ЗАКАЗ"
                  f"\n\nНомер заказа:  {self.id}"
                  f"\nВремя оформления: {created}"
                  f"\n\nТелефон получателя: {self.phone_receiver}"
                  f"\n\nСпособ доставки: {self.delivery_method}"
                  f"\n\nТовары: \n\n{goods_lst}\n"
                  f"Всего: {self.total_price} руб.\n"
                  f"\nСкидка: {self.discount}"
                  f"\n\nВсего к оплате: {self.final_price} руб."
                  f'\n\nДля подтверждения заказа с вами свяжутся в ближайшее время в телеграм или по телефону {self.phone_receiver}')
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
    total_price = models.PositiveIntegerField(default=0)

    def get_total_price(self):
        unit_price = int(self.wear.price)
        self.total_price = int(self.quantity) * unit_price
        self.save()
        result = int(self.total_price)
        return result

    def create_str_in_my_ord_msg(self):
        return f'{self.wear.name}({self.quantity})'


class OrderDolls(DatesModelMixin):
    class Meta:
        verbose_name = "Заказ кукол"
        verbose_name_plural = "Заказы кукол"

    tg_user = models.ForeignKey(TgUser,
                                on_delete=models.CASCADE,
                                verbose_name='Пользователь Телеграм')
    executor = models.ForeignKey(User,
                                 on_delete=models.PROTECT,
                                 verbose_name='Исполнитель',
                                 blank=True,
                                 null=True
                                 )

    goods = models.ManyToManyField(Doll,
                                   blank=True,
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
    total_units_quantity = models.PositiveIntegerField(default=0)