from bot import messages
from bot.interface.buttons import WearSexChoice
from bot.interface.constructors import create_product_menu
from bot.handlers.handlers_funcs import check_availability
from store.constants import WearSex, WearColor, WearSize
from store import models as wear_models


def handle_user_callback(bot, chat_id, call, bot_manager):

    color_list = [col[0] for col in WearColor.choices]
    sizes_list = [i[0] for i in WearSize.choices]
    wear_category = bot_manager.wear_cat

    # Пол
    if call.data == WearSexChoice.MALE.callback_data:
        male_wear = wear_category.objects.filter(sex=WearSex.MALE)
        if check_availability(chat_id, bot, male_wear):
            bot.send_message(chat_id, text='Для мальчика')
            for obj in male_wear:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

    elif call.data == WearSexChoice.FEMALE.callback_data:
        female_wear = wear_category.objects.filter(sex=WearSex.FEMALE)
        if check_availability(chat_id, bot, female_wear):
            bot.send_message(chat_id, text='Для девочки')
            for obj in female_wear:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

    elif call.data == WearSexChoice.UNISEX.callback_data:
        unisex_wear = wear_category.objects.filter(sex=WearSex.UNISEX)
        if check_availability(chat_id, bot, unisex_wear):
            bot.send_message(chat_id, text='Унисекс')
            for obj in unisex_wear:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

    # Бренд

    elif call.data in bot_manager.all_brands_names:
        brand = wear_models.Brand.objects.get(name=call.data)
        brand_wear = wear_category.objects.filter(brand=brand)
        if check_availability(chat_id, bot, brand_wear):
            bot.send_message(chat_id, text=f'{brand.name}')
            for obj in brand_wear:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

    # Размер
    elif call.data in sizes_list:
        wear_by_size = wear_category.objects.filter(size=call.data)
        if check_availability(chat_id, bot, wear_by_size):
            bot.send_message(chat_id, text=f'Размер: {call.data}')
            for obj in wear_by_size:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

    # Цвет
    elif call.data in color_list:
        wear_by_color = wear_category.objects.filter(color=call.data)
        if check_availability(chat_id, bot, wear_by_color):
            bot.send_message(chat_id, text=f'Цвет: {call.data}')
            for obj in wear_by_color:
                bot.send_photo(chat_id, obj.image, caption=messages.create_wear_obj_txt(obj),
                               reply_markup=create_product_menu(obj))

