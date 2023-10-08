from bot.tg_user_actions import TgUserAction, create_submit_order_menu


def get_customer_info(bot, chat_id, message, bot_manager):
    #  Получение телефона пользователя
    if message.startswith(TgUserAction.phone_msg):
        phone = message.lstrip("tel-")
        bot_manager.tg_user.phone = phone
        bot_manager.tg_user.save()
        # Сделать нормальную валидацию телефона
        bot.send_message(chat_id, 'Ваш телефон сохранен')
        bot.send_message(chat_id, f'Пришлите ФИО полуателя в формате {TgUserAction.edit_receiver_name}name-')
        return True

    # Получение ФИО получателя
    elif message.startswith(TgUserAction.send_receiver_name):
        order = bot_manager.current_order
        name = message.lstrip(TgUserAction.send_receiver_name)
        order.receiver = name
        order.save()
        bot.send_message(chat_id, 'ФИО получателя сохранено')
        bot.send_message(chat_id, f'Напишите телефон получателя в формате: {TgUserAction.send_receiver_phone}ТЕЛЕФОН')
        return True

    # Получение телефона получателя
    elif message.startswith(TgUserAction.send_receiver_phone):
        order = bot_manager.current_order
        phone = message.lstrip(TgUserAction.send_receiver_phone)
        order.phone_receiver = phone
        order.save()
        bot.send_message(chat_id, 'Телефон получателя сохранен')
        bot.send_message(chat_id,
                         f'Напишите адрес доставки в формате: {TgUserAction.send_receiver_address}город, улица, дом, квартира, индекс')
        return True

    # Получение адреса получателя
    elif message.startswith(TgUserAction.send_receiver_address):
        order = bot_manager.current_order
        address = message.lstrip(TgUserAction.send_receiver_address)
        order.address = address
        order.save()
        bot.send_message(chat_id, 'Адрес получателя сохранен.\nДавайте проверим, правильно ли составлен заказ')
        bot.send_message(chat_id, order.create_final_order_msg(),
                         reply_markup=create_submit_order_menu())
        return True

    else:
        return False
