from django.utils import timezone
from datetime import timedelta
from sales.models import Order, OrderWearItem
from sales.constants import OrderStatus

# СДЕЛАТЬ ЭТО В ЭТОМ ФАЙЛЕ
# Потом запилить отдельную функцию - повторение с bot/tg_user_actions.py


def delete_outdated_orders(min_interval_after_upt):
    t_after_upt = timedelta(minutes=min_interval_after_upt)
    time_now = timezone.now()
    orders_to_delete = Order.objects.filter(status=OrderStatus.CREATED)
    for order in orders_to_delete:
        if t_after_upt < (time_now - order.updated):
            goods_in_cart = list(order.goods.all())
            wear_items_in_cart_db = OrderWearItem.objects.all()
            for item in goods_in_cart:
                wear_unit_db = wear_items_in_cart_db.get(wear=item,
                                                         order=order)
                print("Количество на складе " + str(item.quantity))
                print("Количество в корзине " + str(wear_unit_db.quantity))
                item.quantity += wear_unit_db.quantity
                item.save()
            print(order)
            order.delete()

