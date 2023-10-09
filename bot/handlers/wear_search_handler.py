from bot import messages
from bot.interface.buttons import SearchWearMenu
from bot.interface.constructors import (create_sex_choice_menu,
                                        create_brand_menu, create_size_menu, create_color_menu, create_product_menu, create_wear_request_menu)


def handle_wear_search(bot, chat_id, message, bot_manager):

    wear_category = bot_manager.wear_cat
    # Все товары категории
    if message == SearchWearMenu.all.text:
        wear_cat_all = wear_category.objects.all()

        for obj in wear_cat_all:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                           reply_markup=create_product_menu(obj))

    # Пол
    elif message == SearchWearMenu.sex_selection.text:
        create_sex_choice_menu(bot=bot,
                               chat_id=chat_id,
                               msg_text=messages.sex_choice)

    # Бренд
    elif message == SearchWearMenu.brand_selection.text:
        create_brand_menu(bot=bot, chat_id=chat_id)

    # Размер
    elif message == SearchWearMenu.size_selection.text:
        create_size_menu(bot=bot,
                         chat_id=chat_id,
                         row_len=2)

    # Цвет
    elif message == SearchWearMenu.color_selection.text:
        create_color_menu(bot=bot,
                          chat_id=chat_id,
                          row_len=2)


