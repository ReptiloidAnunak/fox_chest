from telebot import types
from sales.constants import DeliveryMethods, OFFICE_ADDRESS
from sales.models import Order, OrderStatus
from bot.tg_user_acts_funcs import (start_checkout_order, add_to_cart, delete_from_cart, add_to_favorite,
                                    delete_from_favorite)


class TgUserAction:
    MARKER = "act-"
    add_to_cart = 'add'
    delete_from_cart = 'delete'
    add_to_favorite = 'favorite'
    delete_from_favorite = 'fav_del'
    see_cart = 'cart'
    checkout_order = 'checkout_order'
    empty_cart = 'empty_cart'
    phone_msg = 'tel-'
    get_delivery = 'delivery'
    send_receiver_name = 'name-'
    send_receiver_phone = 'tr-'
    send_receiver_address = 'rad-'

    def __init__(self, action_call):
        self.action_data = action_call.split('-')
        self.action_code = self.action_data[1].split(':')[0]
        self.product_id = self.action_data[1].split(':')[1]

    def route(self, bot_manager, bot, chat_id):
        if self.action_code == self.add_to_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            add_to_cart(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в корзину! 🦊✅\nХотите оформить заказ или добавите что-то ещё?
                                            """)

        elif self.action_code == self.delete_from_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            delete_from_cart(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} удален из корзины! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)

        elif self.action_code == self.add_to_favorite:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            print(product.name)
            add_to_favorite(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в избранное! 🦊❤️\nВ любой момент вы можете посмотреть список заинтересовавших товаров с помощью команды /favorite в Меню
                                            """)

        elif self.action_code == self.delete_from_favorite:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            delete_from_favorite(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} удален из избранного! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)

        elif self.action_code == self.see_cart:
            user_order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                              status=OrderStatus.CREATED).first()

        # Оформить заказ
        elif self.action_code == self.checkout_order:
            start_checkout_order(bot_manager, bot, chat_id, create_delivery_ways_menu())

        # Выбрать способ доставки
        elif self.action_code == self.get_delivery:
            order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED).first()
            order.delivery_method = self.product_id
            order.save()

            if order.delivery_method != DeliveryMethods.PICKUP:
                bot.send_message(chat_id, f'Напишите ФИО получателя в формате {self.send_receiver_name}Фамилия Имя Отчество')
            else:
                bot.send_message(chat_id, f'Вы получите товар по адресу:\n{OFFICE_ADDRESS}. '
                                          f'\nДля подтверждения заказа с вами свяжутся в ближайшее время в телеграм или по телефону {bot_manager.tg_user.phone}')


def create_delivery_ways_menu():
    "Понять, куда девать эту функцию"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=DeliveryMethods.PICKUP,
                                      callback_data=f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.PICKUP}')
    btn2 = types.InlineKeyboardButton(text=DeliveryMethods.POST_OF_RUSSIA,
                                      callback_data=f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.POST_OF_RUSSIA}')
    btn3 = types.InlineKeyboardButton(text=DeliveryMethods.BOXBERRY,
                                      callback_data=f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.BOXBERRY}')
    btn4 = types.InlineKeyboardButton(text=DeliveryMethods.AVITO,
                                      callback_data=f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.AVITO}')
    btn5 = types.InlineKeyboardButton(text=DeliveryMethods.SDEK,
                                      callback_data=f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.SDEK}')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup
