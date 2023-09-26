# https://habr.com/ru/articles/759784/
#

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot, types

from fox_shop.settings import BOT_TOKEN
from bot import messages
from bot.models import TgUser
from bot.buttons import MainMenu, ChildWearMenu
from bot.utils import create_wear_obj_answer
from store import models as wear_models

# python3 manage.py runbot

bot = TeleBot(BOT_TOKEN, threaded=False)


class Command(BaseCommand):
    help = "Run telegram-bot"

    def handle(self, *args, **options):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

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
        def route_requests(message):
            if message.text == ChildWearMenu.t_short:
                tshorts = wear_models.TShort.objects.all()
                for obj in tshorts:
                    bot.send_photo(message.chat.id, obj.image, caption=create_wear_obj_answer(obj))



        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



