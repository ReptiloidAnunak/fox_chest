from telebot import types

from store.models import Wear
from bot.buttons import MainMenu, ChildWearMenu, WearMenu, WearSexChoice


class BotManager:
    def __init__(self):
        self.wear_cat = None




def create_wear_obj_answer(obj: Wear):
    obj_msg = (f"""Товар: {obj.name}
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


def create_wear_request_menu(bot, message, chat_id, msg_text):
    markup = types.InlineKeyboardMarkup()
    btn1 = WearMenu.all
    btn2 = WearMenu.sex_selection
    btn3 = WearMenu.size_selection
    btn4 = WearMenu.color_selection
    btn5 = WearMenu.brand_selection
    # btn6 = MainMenu.question
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
