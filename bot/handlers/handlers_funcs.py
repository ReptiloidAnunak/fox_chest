
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
    if not order.phone_receiver:
        bot.send_message(chat_id, f'Напишите телефон получателя в формате: {code_rec_phone}ТЕЛЕФОН')
        return False
    elif not order.receiver:
        bot.send_message(chat_id, f'Пришлите ФИО полуателя в формате {code_edit_rec_name}Фамилия Имя Отчество')
        return False
    elif not order.address:
        bot.send_message(chat_id,
                         f'Напишите адрес доставки в формате: {code_send_rec_address}город, улица, дом, квартира, индекс')
        return False
    else:
        if bot_manager.is_rec_info_submit == False:
            bot.send_message(chat_id,
                             f'Проверьте сохраненные данные из вашего заказа\n'
                             f'\nИмя получателя: {order.receiver}'
                             f'\nТелефон получателя: {order.phone_receiver}'
                             f'\nАдрес получателя: {order.address}'
                             f'\nВсе верно?',
                             reply_markup=markup)
            return False
        else:
            return True



