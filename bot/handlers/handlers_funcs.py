
def check_availability(chat_id, bot, lst: list):
    if not lst:
        bot.send_message(chat_id, "Нет в наличии")
        return False
    else:
        return True


def check_receiver_info(chat_id, bot, order,
                        code_rec_phone,
                        code_edit_rec_name,
                        code_send_rec_address):
    if not order.phone_receiver:
        bot.send_message(chat_id, f'Напишите телефон получателя в формате: {code_rec_phone}ТЕЛЕФОН')
        return False
    elif not order.receiver:
        bot.send_message(chat_id, f'Пришлите ФИО полуателя в формате {code_edit_rec_name}') #Вот тут косяк
        return False
    elif not order.address:
        bot.send_message(chat_id,
                         f'Напишите адрес доставки в формате: {code_send_rec_address}город, улица, дом, квартира, индекс')
        return False
    else:
        bot.send_message(chat_id,
                         f'Проверьте сохраненные данные из вашего заказа\n'
                         f'\nИмя получателя: {order.receiver}'
                         f'\nТелефон получателя: {order.phone_receiver}'
                         f'\nАдрес получателя: {order.address}'
                         f'\nВсе верно?')
        # Сделать кнопки подтверждения данных пользователя
        return True



