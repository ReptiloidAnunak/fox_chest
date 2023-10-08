from bot import messages
from bot.interface.buttons import ChoiceWearMenu, WearSexChoice
from bot.interface.constructors import (create_sex_choice_menu,
                                        create_brand_menu, create_size_menu, create_color_menu, create_product_menu)

from store.constants import WearSex, WearColor, WearSize
from store import models as wear_models


def handle_wear_search(bot, call, chat_id, bot_manager):

    color_list = [col[0] for col in WearColor.choices]
    sizes_list = [i[0] for i in WearSize.choices]
    wear_category = bot_manager.wear_cat

    # Все товары категории
    if call.data == ChoiceWearMenu.all.callback_data:
        wear_cat_all = wear_category.objects.all()

        for obj in wear_cat_all:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))

    # Пол
    elif call.data == ChoiceWearMenu.sex_selection.callback_data:
        create_sex_choice_menu(bot=bot,
                               chat_id=chat_id,
                               msg_text=messages.sex_choice)

    elif call.data == WearSexChoice.MALE.callback_data:
        male_wear = wear_category.objects.filter(sex=WearSex.MALE)
        bot.send_message(chat_id, text='Для мальчика')
        for obj in male_wear:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))

    elif call.data == WearSexChoice.FEMALE.callback_data:
        female_wear = wear_category.objects.filter(sex=WearSex.FEMALE)
        bot.send_message(chat_id, text='Для девочки')
        for obj in female_wear:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))

    elif call.data == WearSexChoice.UNISEX.callback_data:
        unisex_wear = wear_category.objects.filter(sex=WearSex.UNISEX)
        bot.send_message(chat_id, text='Унисекс')
        for obj in unisex_wear:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))

    # Бренд
    elif call.data == ChoiceWearMenu.brand_selection.callback_data:
        create_brand_menu(bot=bot, chat_id=chat_id)

    elif call.data in bot_manager.all_brands_names:
        brand = wear_models.Brand.objects.get(name=call.data)
        brand_wear = wear_category.objects.filter(brand=brand)
        for obj in brand_wear:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))

    # Размер
    elif call.data == ChoiceWearMenu.size_selection.callback_data:
        create_size_menu(bot=bot,
                         chat_id=chat_id,
                         row_len=2)

    elif call.data in sizes_list:
        wear_by_size = wear_category.objects.filter(size=call.data)
        for obj in wear_by_size:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))


    # Цвет
    elif call.data == ChoiceWearMenu.color_selection.callback_data:
        create_color_menu(bot=bot,
                          chat_id=chat_id,
                          row_len=2)

    elif call.data in color_list:
        wear_by_color = wear_category.objects.filter(color=call.data)
        for obj in wear_by_color:
            bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_answer_txt(obj),
                           reply_markup=create_product_menu(obj))
