from sales.models import Order, OrderStatus, Favorite, OrderWearItem


def add_to_cart(bot, chat_id, bot_manager, product, action):
    if product.quantity > 0:
        product.quantity -= 1
        product.save()

        order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                     status=OrderStatus.CREATED)

        wear_item, created = OrderWearItem.objects.get_or_create(order=order,
                                                        wear=product)
        order.total_units_quantity += 1
        wear_item.quantity += 1
        wear_item.save()

        order.goods.add(product)
        order.save()

        bot.send_message(chat_id,
                         f"""Товар {product.name} (1 ед. - {product.price} р.) добавлен в корзину! Всего в корзине {wear_item.quantity} шт.
                         \n🦊✅\nХотите оформить заказ или добавите что-то ещё?
                                        """,
                         reply_markup=action.create_checkout_order_btn()
                         )

    else:
        bot.send_message(chat_id,
                         f"""Товар {product.name} раскупили! 🦊✅\nПосмотрите другие товары\n⬇️⬇️⬇️
                                        """
                         )


def delete_from_cart(bot_manager, product):
    product.quantity += 1
    product.save()

    order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                 status=OrderStatus.CREATED).first()
    order.goods.remove(product)
    order.total_units_quantity -= 1
    order.save()


def add_to_favorite(bot_manager, product):
    favorite_list, created = Favorite.objects.get_or_create(tg_user=bot_manager.tg_user)
    favorite_list.goods.add(product)
    favorite_list.save()


def delete_from_favorite(bot_manager, product):
    favorite_list = Favorite.objects.filter(tg_user=bot_manager.tg_user).first()
    favorite_list.goods.remove(product)
    favorite_list.save()

