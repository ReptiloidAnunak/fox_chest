from bot.tg_user_actions import TgUserAction, create_submit_order_menu, create_receiver_info_menu
from bot.interface.constructors import create_continue_checkout_menu


def get_customer_info(bot, chat_id, message, bot_manager):
    print('get_customer_info')
    #  Получение телефона пользователя
    if message.startswith(TgUserAction.phone_msg):
        phone = message.lstrip("tel-")
        user = bot_manager.tg_user
        user.phone = phone
        user.save()
        # Сделать нормальную валидацию телефона
        bot.send_message(chat_id, 'Ваш телефон сохранен',
                         reply_markup=create_continue_checkout_menu())
        return True

    # Получение ФИО получателя
    elif message.startswith(TgUserAction.send_receiver_name):
        order = bot_manager.current_order
        name = message.lstrip(TgUserAction.send_receiver_name)
        order.receiver = name
        order.save()
        bot.send_message(chat_id, f'ФИО получателя сохранено.\n\n{order.create_final_order_msg()}',
                         reply_markup=create_continue_checkout_menu())
        return True

    # Получение телефона получателя
    elif message.startswith(TgUserAction.send_receiver_phone):
        order = bot_manager.current_order
        phone = message.lstrip(TgUserAction.send_receiver_phone)
        order.phone_receiver = phone
        order.save()
        bot.send_message(chat_id, f'Телефон получателя сохранен.\n\n{order.create_final_order_msg()}',
                         reply_markup=create_continue_checkout_menu())
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


    elif message.startswith(TgUserAction.edit_receiver_name):
        print("другое имя")

    # Изменение адреса получателя
    elif message.startswith(TgUserAction.edit_receiver_address):
        print("изменить адрес")
        order = bot_manager.current_order
        address = message.lstrip(f'{TgUserAction.edit_receiver_address}-')
        print(address)
        order.address = address
        order.save()
        bot.send_message(chat_id, f'Адрес получателя сохранен.\n\n{order.create_final_order_msg()}',
                         reply_markup=create_receiver_info_menu())
        return True

    # Изменение телефона получателя
    elif message.startswith(TgUserAction.edit_receiver_phone):
        print("другой телефон")
        order = bot_manager.current_order
        phone = message.lstrip(f'{TgUserAction.edit_receiver_phone}-')
        print(phone)
        order.phone_receiver = phone
        order.save()
        bot.send_message(chat_id, f'Телефон получателя сохранен.\n\n{order.create_final_order_msg()}',
                         reply_markup=create_receiver_info_menu())
        return True
    else:
        return False