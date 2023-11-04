from sales.constants import DeliveryMethods, OFFICE_ADDRESS


def check_availability(chat_id, bot, lst: list):
    if not lst:
        bot.send_message(chat_id, "Нет в наличии")
        return False
    else:
        return True


def check_receiver_info(chat_id, bot, bot_manager,
                        order,
                        code_rec_phone,
                        code_edit_rec_name,
                        code_send_rec_address,
                        markup):
    print('check_receiver_info')

    if not bot_manager.tg_user.phone:
        bot.send_message(chat_id, f'Напишите ваш телефон для связи в формате:\ntel-ТЕЛЕФОН'
                                  f'\nПРИМЕР: tel-8916*******')
        return False


    elif (not order.phone_receiver and bot_manager.current_order.delivery_method not in
          [DeliveryMethods.PICKUP, DeliveryMethods.UNKNOWN]):
        bot.send_message(chat_id, f'Напишите телефон получателя в формате:\n{code_rec_phone}ТЕЛЕФОН'
                                  f'\nПРИМЕР: {code_rec_phone}8916*******')
        return False

    elif not order.receiver:
        bot.send_message(chat_id, f'Пришлите ФИО полуателя в формате:\n{code_edit_rec_name}Фамилия Имя Отчество'
                                  f'\nПРИМЕР: {code_edit_rec_name} Иванов Иван Иванович')
        return False

    elif not order.address and bot_manager.current_order.delivery_method != DeliveryMethods.PICKUP:
        bot.send_message(chat_id,
                         f'Напишите адрес доставки в формате:\n{code_send_rec_address}город,улица, дом, квартира, индекс'
                         f'\nПРИМЕР: {code_send_rec_address}Москва, ул. Пушкина, д.5 к.1, кв. 197, 111111'
                         )
        return False

    else:
        if bot_manager.is_rec_info_submit == False:
            order = bot_manager.current_order
            if bot_manager.current_order.delivery_method == DeliveryMethods.PICKUP:
                order.address = OFFICE_ADDRESS
                order.phone_receiver = bot_manager.tg_user.phone
                # order.receiver = bot_manager.tg_user.first_name + " " + bot_manager.tg_user.last_name
                order.save()
            bot.send_message(chat_id,
                             f'Проверьте сохраненные данные из вашего заказа\n'
                             f'\nCпособ доставки: {order.delivery_method}'
                             f'\nИмя получателя: {order.receiver}'
                             f'\nТелефон получателя: {order.phone_receiver}'
                             f'\nАдрес получателя: {order.address}'
                             f'\nВсе верно?',
                             reply_markup=markup)
            return False
        else:
            return True



