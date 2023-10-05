from telebot import types
from sales.constants import DeliveryMethods
from sales.models import Order, OrderStatus, Favorite


def add_to_cart(bot_manager, product):
    order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                 status=OrderStatus.CREATED)
    order.goods.add(product)
    order.save()


def delete_from_cart(bot_manager, product): # Команда выполняется только когда я нажимаю "/start". Надо ИСПРВИТЬ!
    order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                 status=OrderStatus.CREATED).first()
    order.goods.remove(product)
    order.save()


def add_to_favorite(bot_manager, product):
    favorite_list, created = Favorite.objects.get_or_create(tg_user=bot_manager.tg_user)
    favorite_list.goods.add(product)
    favorite_list.save()


def delete_from_favorite(bot_manager, product):
    favorite_list = Favorite.objects.filter(tg_user=bot_manager.tg_user)
    favorite_list.goods.remove(product)
    favorite_list.save()


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
            bot.send_message(chat_id, f"""Товар {product.name} удален из избранного! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)

        elif self.action_code == self.see_cart:
            user_order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                              status=OrderStatus.CREATED).first()

        elif self.action_code == self.checkout_order:
            tg_user = bot_manager.tg_user
            order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED).first()
            if tg_user.phone is None:
                bot.send_message(chat_id, "Введите свой телефон для связи в формате tel-ВАШ-НОМЕР-ТЕЛЕФОНА") # Придумать правильный формат

            else:
                user_order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user.id,
                                                                  status=OrderStatus.CREATED)
                order_msg = user_order.create_order_msg()
                bot.send_message(chat_id, order_msg, reply_markup=create_delivery_ways_menu(order))

        elif self.action_code == self.get_delivery:
            order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED).first()
            order.delivery_method = self.product_id
            order.save()

            if order.delivery_method != DeliveryMethods.PICKUP:
                bot.send_message(chat_id, f'Напишите ФИО получателя в формате {self.send_receiver_name}Фамилия Имя Отчество')



def create_delivery_ways_menu(order):
    "Понять, куда девать эту функцию"
    order_id = order.id
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
