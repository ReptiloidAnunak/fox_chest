# https://habr.com/ru/articles/759784/

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot, types

from fox_shop.settings import BOT_TOKEN
from bot import messages
from bot.models import TgUser
from bot.buttons import MainMenu, ChildWearMenu, WearMenu, WearSexChoice
from bot.utils import (BotManager, create_wear_obj_answer,
                       create_wear_request_menu, create_sex_choice_menu,
                       create_brand_menu, create_size_menu, create_color_menu,
                       check_tg_user)
from store.constants import WearSex, WearColor, WearSize
from store import models as wear_models

# python3 manage.py runbot


bot = TeleBot(BOT_TOKEN, threaded=False)

bot_manager = BotManager()


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

            check_tg_user(message, bot_manager)

            bot.send_message(message.chat.id,
                             text=messages.write_greetings(bot_manager),
                             reply_markup=markup
                             )

        @bot.message_handler(content_types=['text'])
        def route_msg_requests(message):
            chat_id = message.chat.id
            if message.text == ChildWearMenu.t_short.text:
                bot_manager.wear_cat = wear_models.TShort
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=messages.tshort_presentation)
            else:
                bot.send_message(chat_id,
                                 text=messages.unknown_command)

        @bot.callback_query_handler(func=lambda call: True)
        def handle_callbacks(call):
            """Handles all callbacks in the chat"""

            chat_id = call.message.chat.id
            wear_category = bot_manager.wear_cat
            color_list = [col[0] for col in WearColor.choices]
            sizes_list = [i[0] for i in WearSize.choices]


            # # # Принцип поиска

            # Все товары категории
            if call.data == WearMenu.all.callback_data:
                wear_cat_all = wear_category.objects.all()

                for obj in wear_cat_all:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))

            # Пол
            elif call.data == WearMenu.sex_selection.callback_data:
                create_sex_choice_menu(bot=bot, message=messages,
                                       chat_id=chat_id,
                                       msg_text=messages.sex_choice)

            elif call.data == WearSexChoice.MALE.callback_data:
                male_wear = wear_category.objects.filter(sex=WearSex.MALE)
                bot.send_message(chat_id, text='Для мальчика')
                for obj in male_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))

            elif call.data == WearSexChoice.FEMALE.callback_data:
                female_wear = wear_category.objects.filter(sex=WearSex.FEMALE)
                bot.send_message(chat_id, text='Для девочки')
                for obj in female_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))

            elif call.data == WearSexChoice.UNISEX.callback_data:
                unisex_wear = wear_category.objects.filter(sex=WearSex.UNISEX)
                bot.send_message(chat_id, text='Унисекс')
                for obj in unisex_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))

            # Бренд
            elif call.data == WearMenu.brand_selection.callback_data:
                create_brand_menu(bot=bot, message=messages, chat_id=chat_id)

            # Размер
            elif call.data == WearMenu.size_selection.callback_data:
                create_size_menu(bot=bot,
                                 message=messages,
                                 chat_id=chat_id,
                                 row_len=2)

            elif call.data in sizes_list:
                wear_by_size = wear_category.objects.filter(size=call.data)
                for obj in wear_by_size:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))



            # Цвет
            elif call.data == WearMenu.color_selection.callback_data:
                create_color_menu(bot=bot,
                                  message=messages,
                                  chat_id=chat_id,
                                  row_len=2)

            elif call.data in color_list:
                wear_by_color = wear_category.objects.filter(color=call.data)
                for obj in wear_by_color:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer(obj))

        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



