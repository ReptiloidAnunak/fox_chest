from telebot import types
from store.models import Wear, Brand
from store.constants import WearSize, WearColor
from bot.buttons import WearMenu, WearSexChoice, OrderMenu
from bot.models import TgUser
from bot.tg_user_actions import TgUserAction


def get_bands_names_list():
    return list(Brand.objects.values_list('name', flat=True))


class BotManager:
    def __init__(self):
        self.tg_user: TgUser = None
        self.is_tg_user_new = False
        self.wear_cat: Wear = None
        self.all_brands_names = get_bands_names_list()


def check_tg_user(message, bot_manager: BotManager):
    tg_user_data = message.from_user
    tg_uid = tg_user_data.id
    obj, created = TgUser.objects.get_or_create(tg_user_id=tg_uid,
                                                  tg_chat_id=message.chat.id,
                                                  first_name=tg_user_data.first_name,
                                                  last_name=tg_user_data.last_name,
                                                  username=tg_user_data.username)
    bot_manager.tg_user = obj


def create_wear_obj_answer_txt(obj: Wear):

    obj_msg = (
                f"""
Товар: {obj.name}
Размер: {obj.size}
Цвет: {obj.color}
Материал: {obj.material}
Пол: {obj.sex}
Возраст: {obj.age}
Марка: {obj.brand}
Цена: {obj.price}
Описание: {obj.description}
                """)
    return obj_msg





def create_order_menu():
    markup = types.InlineKeyboardMarkup()
    btn1 = OrderMenu.my_cart
    btn2 = OrderMenu.checkout_order
    btn3 = OrderMenu.clear_cart
    markup.add(btn1, btn2, btn3)
    return markup

####################################################################


def create_product_menu(product: Wear):
    prod_id = product.id
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="💰✅",
                                      callback_data=f'{TgUserAction.MARKER}add:{prod_id}')
    btn2 = types.InlineKeyboardButton(text="❤️",
                                      callback_data=f'{TgUserAction.MARKER}favorite:{prod_id}')
    btn3 = types.InlineKeyboardButton(text="❌",
                                      callback_data=f'{TgUserAction.MARKER}delete:{prod_id}')
    markup.add(btn1, btn2, btn3)
    return markup


def create_obj_menu_in_favorite(product: Wear, bot_manager: BotManager):
    prod_id = product.id
    bot_manager.wear_cat = type(product)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="💰✅",
                                      callback_data=f'{TgUserAction.MARKER}add:{prod_id}')
    btn2 = types.InlineKeyboardButton(text="❌",
                                      callback_data=f'{TgUserAction.MARKER}fav_del:{prod_id}')
    markup.add(btn1, btn2)
    return markup


def create_obj_menu_in_cart(product: Wear, bot_manager: BotManager):
    prod_id = product.id
    bot_manager.wear_cat = type(product)
    print(type(product))
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="❤️",
                                      callback_data=f'{TgUserAction.MARKER}favorite:{prod_id}')
    btn2 = types.InlineKeyboardButton(text="❌",
                                      callback_data=f'{TgUserAction.MARKER}delete:{prod_id}')
    markup.add(btn1, btn2)
    return markup
####################################################################


def create_wear_request_menu(bot, message, chat_id, msg_text):
    markup = types.InlineKeyboardMarkup()
    btn1 = WearMenu.all
    btn2 = WearMenu.sex_selection
    btn3 = WearMenu.size_selection
    btn4 = WearMenu.color_selection
    btn5 = WearMenu.brand_selection
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(chat_id,
                     text=msg_text,
                     reply_markup=markup
                     )


def create_sex_choice_menu(bot, message, chat_id, msg_text):
    markup = types.InlineKeyboardMarkup()
    btn1 = WearSexChoice.MALE
    btn2 = WearSexChoice.FEMALE
    btn3 = WearSexChoice.UNISEX
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(chat_id,
                     text=msg_text,
                     reply_markup=markup
                     )


def create_brand_menu(bot, message, chat_id):
    markup = types.InlineKeyboardMarkup()
    brands = Brand.objects.all()
    brand_buttons = []
    for brand in brands:
        brand_btn = types.InlineKeyboardButton(text=brand.name,
                                               callback_data=brand.name)
        brand_buttons.append(brand_btn)
    for btn in brand_buttons:
        markup.row(btn)
    bot.send_message(chat_id,
                     text="Выберите бренд",
                     reply_markup=markup)


def create_size_menu(bot, message, chat_id, row_len: int):
    markup = types.InlineKeyboardMarkup()
    sizes = WearSize.choices
    size_buttons = []

    for s in sizes:
        size_btn = types.InlineKeyboardButton(text=s[0],
                                              callback_data=s[0])
        size_buttons.append(size_btn)

    for i in range(0, len(size_buttons), row_len):
        row_buttons = size_buttons[i:i + row_len]
        markup.row(*row_buttons)
    bot.send_message(chat_id, text="Выберите размер",
                     reply_markup=markup)


def create_color_menu(bot, message, chat_id, row_len: int):
    markup = types.InlineKeyboardMarkup()
    colors = WearColor.choices
    size_buttons = []

    for c in colors:
        size_btn = types.InlineKeyboardButton(text=c[0],
                                              callback_data=c[0])
        size_buttons.append(size_btn)

    for i in range(0, len(size_buttons), row_len):
        row_buttons = size_buttons[i:i + row_len]
        markup.row(*row_buttons)
    bot.send_message(chat_id, text="Выберите цвет",
                     reply_markup=markup)


