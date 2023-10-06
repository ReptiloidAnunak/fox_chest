# https://habr.com/ru/articles/759784/

from django.core.management.base import BaseCommand
import logging
from telebot import TeleBot, types

from fox_shop.settings import BOT_TOKEN

from bot import messages
from bot.tg_user_actions import TgUserAction, create_delivery_ways_menu
from bot.tg_user_acts_funcs import start_checkout_order
from bot.buttons import MainMenu, ChildWearMenu, WearMenu, WearSexChoice
from bot.utils import (BotManager, create_wear_obj_answer_txt,
                       create_wear_request_menu, create_sex_choice_menu,
                       create_brand_menu, create_size_menu, create_color_menu,
                       check_tg_user, create_product_menu, create_obj_menu_in_favorite,
                       create_obj_menu_in_cart, create_order_menu, get_current_order)

from bot.messages import WearPresentations

from store.constants import WearSex, WearColor, WearSize
from store import models as wear_models

from sales.models import Order, OrderStatus, Favorite

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
            btn7 = MainMenu.checkout_order
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

            check_tg_user(message, bot_manager)

            bot.send_message(message.chat.id,
                             text=messages.write_greetings(bot_manager),
                             reply_markup=markup
                             )

        @bot.message_handler(commands=['cart'])
        def get_my_cart(message):
            chat_id = message.chat.id
            check_tg_user(message, bot_manager)
            get_current_order(bot_manager)
            cart, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED)

            goods = list(cart.goods.all())

            if not goods:
                bot.send_message(chat_id, text=messages.cart_is_empty)

            else:
                bot.send_message(chat_id, text="Ваша корзина 🛒")
                for obj in goods:
                    bot.send_photo(chat_id, obj.image,
                                   caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_obj_menu_in_cart(obj, bot_manager))
                bot.send_message(chat_id, text="Хотите оформить заказ?", reply_markup=create_order_menu())

        @bot.message_handler(commands=['favorite'])
        def get_my_favorite(message):
            chat_id = message.chat.id
            check_tg_user(message, bot_manager)
            fav_lst, created = Favorite.objects.get_or_create(tg_user=bot_manager.tg_user)

            goods = list(fav_lst.goods.all())

            if not goods:
                bot.send_message(chat_id, text="Ваш список избранного пуст")
            else:
                bot.send_message(chat_id, text="Ваши избранные товары: 🛒")
                for obj in goods:
                    bot.send_photo(chat_id, obj.image,
                                   caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_obj_menu_in_favorite(obj, bot_manager))

        @bot.message_handler(content_types=['text'])
        def route_msg_requests(message):
            """ !!! Этот код слишком длинный, надо написать потом нормальную функцию"""
            check_tg_user(message, bot_manager)
            get_current_order(bot_manager)
            chat_id = message.chat.id
            message = message.text

            if message == MainMenu.checkout_order.text:
                start_checkout_order(bot_manager, bot, chat_id,
                                     markup=create_delivery_ways_menu())

            elif message == ChildWearMenu.t_short.text:
                bot_manager.wear_cat = wear_models.TShort
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=WearPresentations.tshort_presentation,
                                         )

            elif message == ChildWearMenu.pants.text:
                bot_manager.wear_cat = wear_models.Pants
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=WearPresentations.pants_presentation)

            elif message == ChildWearMenu.jacket.text:
                bot_manager.wear_cat = wear_models.Jacket
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=WearPresentations.jacket_presentation)

            elif message == ChildWearMenu.bodysuit.text:
                bot_manager.wear_cat = wear_models.Bodysuit
                create_wear_request_menu(bot=bot, message=message,
                                         chat_id=chat_id,
                                         msg_text=WearPresentations.bodysuit_presentation)
            #     Разобраться с телефоном
            elif message.startswith(TgUserAction.phone_msg):
                phone = message.lstrip("tel-")
                bot_manager.tg_user.phone = phone
                bot_manager.tg_user.save()
                #Сделать нормальную валидацию телефона
                bot.send_message(chat_id, 'Телефон сохранен')

            # Получение ФИО получателя
            elif message.startswith(TgUserAction.send_receiver_name):
                order = bot_manager.current_order
                name = message.lstrip(TgUserAction.send_receiver_name)
                order.receiver = name
                order.save()
                bot.send_message(chat_id, 'ФИО получателя сохранено')
                bot.send_message(chat_id, f'Напишите телефон получателя в формате: {TgUserAction.send_receiver_phone}ТЕЛЕФОН')

            # Получение телефона получателя
            elif message.startswith(TgUserAction.send_receiver_phone):
                order = bot_manager.current_order
                phone = message.lstrip(TgUserAction.send_receiver_phone)
                order.phone_receiver = phone
                order.save()
                bot.send_message(chat_id, 'Телефон получателя сохранен')
                bot.send_message(chat_id,
                                 f'Напишите адрес доставки в формате: {TgUserAction.send_receiver_address}город, улица, дом, квартира, индекс')

            elif message.startswith(TgUserAction.send_receiver_address):
                order = bot_manager.current_order
                address = message.lstrip(TgUserAction.send_receiver_address)
                order.address = address
                order.save()
                bot.send_message(chat_id, 'Адрес получателя сохранен.\nДавайте проверим, правильно ли составлен заказ')
                bot.send_message(chat_id, order.create_final_order_msg())

            else:
                print(message)
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
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            # Пол
            elif call.data == WearMenu.sex_selection.callback_data:
                create_sex_choice_menu(bot=bot, message=messages,
                                       chat_id=chat_id,
                                       msg_text=messages.sex_choice)

            elif call.data == WearSexChoice.MALE.callback_data:
                male_wear = wear_category.objects.filter(sex=WearSex.MALE)
                bot.send_message(chat_id, text='Для мальчика')
                for obj in male_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            elif call.data == WearSexChoice.FEMALE.callback_data:
                female_wear = wear_category.objects.filter(sex=WearSex.FEMALE)
                bot.send_message(chat_id, text='Для девочки')
                for obj in female_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            elif call.data == WearSexChoice.UNISEX.callback_data:
                unisex_wear = wear_category.objects.filter(sex=WearSex.UNISEX)
                bot.send_message(chat_id, text='Унисекс')
                for obj in unisex_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            # Бренд
            elif call.data == WearMenu.brand_selection.callback_data:
                create_brand_menu(bot=bot, message=messages, chat_id=chat_id)

            elif call.data in bot_manager.all_brands_names:
                brand = wear_models.Brand.objects.get(name=call.data)
                brand_wear = wear_category.objects.filter(brand=brand)
                for obj in brand_wear:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            # Размер
            elif call.data == WearMenu.size_selection.callback_data:
                create_size_menu(bot=bot,
                                 message=messages,
                                 chat_id=chat_id,
                                 row_len=2)

            elif call.data in sizes_list:
                wear_by_size = wear_category.objects.filter(size=call.data)
                for obj in wear_by_size:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))


            # Цвет
            elif call.data == WearMenu.color_selection.callback_data:
                create_color_menu(bot=bot,
                                  message=messages,
                                  chat_id=chat_id,
                                  row_len=2)

            elif call.data in color_list:
                wear_by_color = wear_category.objects.filter(color=call.data)
                for obj in wear_by_color:
                    bot.send_photo(chat_id, obj.image, caption=create_wear_obj_answer_txt(obj),
                                   reply_markup=create_product_menu(obj))

            # Обработка действий пользователя
            elif call.data.startswith(TgUserAction.MARKER):
                get_current_order(bot_manager)
                action = TgUserAction(call.data)
                action.route(bot_manager, bot, chat_id)

        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()



