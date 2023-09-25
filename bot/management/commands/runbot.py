# https://habr.com/ru/articles/759784/
#

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot

from fox_shop.settings import BOT_TOKEN
from bot import messages
from bot.models import TgUser

# python3 manage.py runbot

bot = TeleBot(BOT_TOKEN, threaded=False)


class Command(BaseCommand):
    help = "Run telegram-bot"

    def handle(self, *args, **options):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        @bot.message_handler(commands=['help', 'start'])
        def send_welcome(message):
            bot.reply_to(message, messages.greetings)

        @bot.message_handler(func=lambda message: True)
        def echo_message(message):
            bot.reply_to(message, message.text)


        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



