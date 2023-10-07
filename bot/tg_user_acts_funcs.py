from sales.models import Order, OrderStatus, Favorite


def add_to_cart(bot_manager, product):
    order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                 status=OrderStatus.CREATED)
    order.goods.add(product)
    order.save()


def delete_from_cart(bot_manager, product): # Команда выполняется только когда я нажимаю "/start". Надо ИСПРВИТЬ!
    order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                 status=OrderStatus.CREATED).first()
    order.goods.remove(product)
    order.save()


def add_to_favorite(bot_manager, product):
    favorite_list, created = Favorite.objects.get_or_create(tg_user=bot_manager.tg_user)
    favorite_list.goods.add(product)
    favorite_list.save()


def delete_from_favorite(bot_manager, product):
    favorite_list = Favorite.objects.filter(tg_user=bot_manager.tg_user).first()
    favorite_list.goods.remove(product)
    favorite_list.save()


def start_checkout_order(bot_manager, bot, chat_id, markup):
    tg_user = bot_manager.tg_user
    order = bot_manager.current_order
    if tg_user.phone is None:
        bot.send_message(chat_id,
                         "Введите свой телефон для связи в формате tel-ВАШ-НОМЕР-ТЕЛЕФОНА")  # Придумать правильный формат

    else:
        user_order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                          status=OrderStatus.CREATED)
        order_msg = user_order.create_order_msg()
        bot.send_message(chat_id, order_msg, reply_markup=markup)