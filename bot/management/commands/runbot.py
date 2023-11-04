# https://habr.com/ru/articles/759784/

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot

from fox_shop.settings import BOT_TOKEN
# accept_order
from bot.handlers.wear_cat_handler import handle_wear_cat_request
from bot.handlers.tg_user_info_handler import get_customer_info
from bot.handlers.commands_handler import route_commands
from bot.handlers.wear_search_handler import handle_wear_search
from bot.handlers.search_callback_handler import handle_user_callback
from bot.tg_user_actions import TgUserAction
from bot.bot_manager import (BotManager, check_tg_user, get_current_order)

# python3 manage.py runbot

"""Сделать нормальную обработку ошибок!!!!!!"""

bot = TeleBot(BOT_TOKEN, threaded=False)

bot_manager = BotManager()


class Command(BaseCommand):
    help = "Run telegram-bot"

    def handle(self, *args, **options):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        @bot.message_handler(commands=['start', 'cart', 'favorite'])
        def handle_commands(message):
            route_commands(bot, message, bot_manager)

        @bot.message_handler(content_types=['text'])
        def handle_msg_requests(message):
            check_tg_user(message, bot_manager)
            get_current_order(bot_manager)
            chat_id = message.chat.id
            message = message.text
            try:
                handle_wear_cat_request(bot, chat_id, message, bot_manager)
                handle_wear_search(bot, chat_id, message, bot_manager)
                get_customer_info(bot, chat_id, message, bot_manager)
            except:
                print('Ошибка в фунции')

        # Обработка коллбеков
        @bot.callback_query_handler(func=lambda call: True)
        def handle_callbacks(call):
            """Handles all callbacks in the chat"""
            chat_id = call.message.chat.id
            # check_tg_user(message, bot_manager)
            get_current_order(bot_manager)
            # Обработка действий пользователя
            if call.data.startswith(TgUserAction.MARKER):
                get_current_order(bot_manager)
                action = TgUserAction(call.data)
                action.route(bot_manager, bot, chat_id)

            # Обработка поиска одежды по параметрам
            else:
                handle_user_callback(bot, chat_id, call, bot_manager)

        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



