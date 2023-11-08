from bot.interface.constructors import create_start_keyboard, create_cat_wear_keyboard


def back_to_main_menu(bot, chat_id):
    bot.send_message(chat_id=chat_id,
                     text="Вы вернулись в Главное Меню",
                     reply_markup=create_start_keyboard()
                     )


def back_to_wear_cat_menu(bot, chat_id):
    bot.send_message(chat_id=chat_id,
                     reply_markup=create_cat_wear_keyboard(bot, chat_id,
                                                           msg_text="Вы вернулись к выбору категорий")
                     )
