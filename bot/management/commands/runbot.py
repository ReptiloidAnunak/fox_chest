# https://habr.com/ru/articles/759784/
#

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot, types

from fox_shop.settings import BOT_TOKEN
from bot import messages
from bot.models import TgUser
from bot.buttons import MainMenu, ChildWearMenu, WearMenu
from bot.utils import create_wear_obj_answer, create_wear_request_menu
from store import models as wear_models

# python3 manage.py runbot


class BotManager:
    def __init__(self):
        self.wear_cat = None


bot = TeleBot(BOT_TOKEN, threaded=False)

bot_manager = BotManager()

wear_category = None



class Command(BaseCommand):
    help = "Run telegram-bot"

    def handle(self, *args, **options):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        wear_category = None

        @bot.message_handler(commands=['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = ChildWearMenu.t_short
            btn2 = ChildWearMenu.pants
            btn3 = ChildWearMenu.jacket
            btn4 = ChildWearMenu.bodysuit
            btn5 = MainMenu.macrame_doll_btn
            btn6 = MainMenu.question
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.chat.id,
                             text=messages.greetings,
                             reply_markup=markup
                             )

        @bot.message_handler(content_types=['text'])
        def route_msg_requests(message):
            global wear_category
            chat_id = message.chat.id
            if message.text == ChildWearMenu.t_short.text:
                wear_category = wear_models.TShort
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=messages.tshort_presentation)
                return wear_category
            else:
                bot.send_message(chat_id,
                                 text=messages.unknown_command)


        @bot.callback_query_handler(func=lambda call: True)
        def handle_callbacks(call):
            """Handles all collbacks in the chat"""
            global wear_category
            chat_id = call.message.chat.id
            if call.data == WearMenu.all.callback_data:
                bot.send_message(chat_id, text="Ща все покажу")
                wear_cat_all = wear_category.objects.all()
                for obj in wear_cat_all:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))


        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



