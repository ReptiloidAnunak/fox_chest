from telebot import types

from store.models import Wear
from sales.constants import OrderStatus, DeliveryMethods, OFFICE_ADDRESS
from sales.models import Order, OrderStatus

from bot.tg_user_acts_funcs import (start_checkout_order, add_to_cart, delete_from_cart, add_to_favorite,
                                    delete_from_favorite)
from bot.handlers.handlers_funcs import check_receiver_info


class TgUserAction:
    MARKER = "act-"

    add_to_cart = 'add'
    delete_from_cart = 'delete'
    see_cart = 'cart'
    empty_cart = 'empty_cart'

    add_to_favorite = 'favorite'
    delete_from_favorite = 'fav_del'

    checkout_order = 'checkout_order'
    submit_order_1 = 'submit_order_1'
    submit_order_2 = 'submit_order_2'

    edit_order = 'edit_order'
    edit_delivery = 'edit_delivery'
    edit_receiver_name = 'edit_receiver_name'
    edit_receiver_phone = 'edit_receiver_phone'
    edit_receiver_address = 'edit_receiver_adrs'
    submit_receiver_info = 'rec_info_ok'
    edit_cart = 'edit_cart'

    phone_msg = 'tel-'
    get_delivery = 'delivery'
    send_receiver_name = 'name-'
    send_receiver_phone = 'tr-'
    send_receiver_address = 'rad-'


    def __init__(self, action_call):
        self.action_data = action_call.split('-')
        self.action_code = self.action_data[1].split(':')[0]
        self.product_id = self.action_data[1].split(':')[1]

    def create_checkout_order_btn(self, product):
        prod_id = product.id
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Оформить заказ",
                                          callback_data=f'{self.MARKER}{self.get_delivery}:order')
        markup.add(btn1)
        return markup

    def save_delivery_method(self, order):
        if self.product_id in [DeliveryMethods.POST_OF_RUSSIA, DeliveryMethods.SDEK,
                               DeliveryMethods.AVITO, DeliveryMethods.BOXBERRY, DeliveryMethods.PICKUP]:
            order.delivery_method = self.product_id
            order.save()


    def route(self, bot_manager, bot, chat_id):
        print("\naction_code " + self.action_code)
        print('product_id ' + self.product_id)

        print("заказ подтвержден - " + str(bot_manager.is_rec_info_submit) + "\n")

        if self.action_code == self.add_to_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            add_to_cart(bot, chat_id, bot_manager, product, action=self)

        elif self.action_code == self.delete_from_cart:
            product = Wear.objects.get(id=self.product_id)
            delete_from_cart(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} удален из корзины! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)

        elif self.action_code == self.add_to_favorite:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
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
            # start_checkout_order(bot_manager, bot, chat_id, create_delivery_ways_menu())
            check_receiver_info(chat_id, bot,
                                bot_manager,
                                order=bot_manager.current_order,
                                code_rec_phone=self.send_receiver_phone,
                                code_edit_rec_name=self.send_receiver_name,
                                code_send_rec_address=self.send_receiver_address,
                                markup=create_receiver_info_menu()
                                )


        # Выбрать способ доставки

        elif self.action_code == self.get_delivery:
            order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED).first()

            self.save_delivery_method(order)


            if order.delivery_method == DeliveryMethods.UNKNOWN:
                bot.send_message(chat_id,
                                 text=f'Выберите способ доставки',
                                 reply_markup=create_delivery_ways_menu())


            elif order.delivery_method == DeliveryMethods.PICKUP:
                print('Самовывоз')

                bot.send_message(chat_id, f'\nСпособ доставки: {order.delivery_method}'
                                          f'Вы получите товар по адресу:\n{OFFICE_ADDRESS}. '
                                          f'\nДля подтверждения заказа с вами свяжутся в ближайшее время в телеграм или по телефону {bot_manager.tg_user.phone}')

            elif (order.delivery_method in [DeliveryMethods.POST_OF_RUSSIA, DeliveryMethods.SDEK,
                                           DeliveryMethods.AVITO, DeliveryMethods.BOXBERRY]):
                self.save_delivery_method(order)
                print('дистанционный')
                check_receiver_info(chat_id, bot,
                                    bot_manager,
                                    order=bot_manager.current_order,
                                    code_rec_phone=self.send_receiver_phone,
                                    code_edit_rec_name=self.send_receiver_name,
                                    code_send_rec_address=self.send_receiver_address,
                                    markup=create_receiver_info_menu()
                                    )


        # ============================================= В отдельную функцию =================================

        # ========================ЛОГИКА ЭТОЙ ФУНКЦИИ АБСОЛЮТНО ПАРАШНАЯ НАДО ПЕРЕСМОТРЕТЬ==================================================================
        # Выбор параметров заказа для изменения
        elif self.action_code == self.edit_order and bot_manager.is_rec_info_submit is False:
            bot.send_message(chat_id, text="Какой параметр вашего заказа хотите изменить?",
                             reply_markup=create_edit_order_menu())

            # Обработка изменений в заказе
            if self.product_id == self.edit_receiver_name:
                print("edit name")
                bot.send_message(chat_id,
                                 f'Напишите ФИО получателя в формате: {self.send_receiver_name} Фамилия Имя Отчество')

            elif self.product_id == self.send_receiver_phone:
                print('edit phone')
                bot.send_message(chat_id, f'Напишите телефон получателя в формате: {self.send_receiver_phone}ТЕЛЕФОН')

            elif self.product_id == self.edit_receiver_address:
                print('edit address')
                bot.send_message(chat_id,
                                 f'Напишите адрес доставки в формате: {self.edit_receiver_address}город, улица, дом, квартира, индекс')

        elif self.action_code == self.edit_order and bot_manager.is_rec_info_submit is True:
            bot.send_message(chat_id, text="Наш менеджер свяжется с Вами для уточнения деталей заказа")

        # ======================================================================================================

            # Оставить сохраненную информацию о получателе без изменений
        elif self.action_code == self.submit_receiver_info:
            print("да")
            bot_manager.current_order.status = OrderStatus.IN_PROGRESS
            bot_manager.current_order.save()
            bot_manager.is_rec_info_submit = True
            bot.send_message(chat_id, f'\nДля подтверждения заказа с вами свяжутся в ближайшее время в телеграм или по телефону {bot_manager.tg_user.phone}')


        #Оставить заказ без изменений 1
        elif self.action_code == self.submit_order_1:
            print("да 1")
            bot_manager.current_order.status = OrderStatus.IN_PROGRESS
            bot_manager.current_order.save()
            bot_manager.is_rec_info_submit = True
            bot.send_message(chat_id,
                             f'\n{bot_manager.tg_user.first_name}, спасибо за заказ! С Вами свяжется наш менеджер в ближайшее время в телеграм или по телефону {bot_manager.tg_user.phone}')

        # Последнее подтверждение заказа
        elif self.action_code == self.submit_order_2:
            print("да 2")
            bot_manager.current_order.status = OrderStatus.IN_PROGRESS
            bot_manager.current_order.save()
            bot_manager.is_rec_info_submit = True
            bot.send_message(chat_id,
                             f'\n{bot_manager.tg_user.first_name}, спасибо за заказ! С Вами свяжется наш менеджер в ближайшее время в телеграм или по телефону {bot_manager.tg_user.phone}')



def create_delivery_ways_menu():
    "Понять, куда девать эту функцию"
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=DeliveryMethods.PICKUP,
                                      callback_data=
                                      f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.PICKUP}')
    btn2 = types.InlineKeyboardButton(text=DeliveryMethods.POST_OF_RUSSIA,
                                      callback_data=
                                      f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.POST_OF_RUSSIA}')
    btn3 = types.InlineKeyboardButton(text=DeliveryMethods.BOXBERRY,
                                      callback_data=
                                      f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.BOXBERRY}')
    btn4 = types.InlineKeyboardButton(text=DeliveryMethods.AVITO,
                                      callback_data=
                                      f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.AVITO}')
    btn5 = types.InlineKeyboardButton(text=DeliveryMethods.SDEK,
                                      callback_data=
                                      f'{TgUserAction.MARKER}{TgUserAction.get_delivery}:{DeliveryMethods.SDEK}')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


def create_submit_order_menu():
    markup = types.InlineKeyboardMarkup()
    btn_submit = types.InlineKeyboardButton(text='✅ Подтвердить заказ',
                                            callback_data=f'{TgUserAction.MARKER}{TgUserAction.submit_order_1}:order')
    btn_edit = types.InlineKeyboardButton(text="✏️ Изменить заказ",
                                          callback_data=
                                          f'{TgUserAction.MARKER}{TgUserAction.edit_order}:order')
    markup.add(btn_submit, btn_edit)
    return markup


def create_receiver_info_menu():
    markup = types.InlineKeyboardMarkup()
    btn_submit_info = types.InlineKeyboardButton('Все верно',
                                                 callback_data=f'{TgUserAction.MARKER}{TgUserAction.submit_receiver_info}:order')
    btn_receiver_name = types.InlineKeyboardButton('Изменить имя',
                                                   callback_data=
                                                   f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_name}'
                                                   )

    btn_receiver_phone = types.InlineKeyboardButton('Изменить телефон',
                                                    callback_data=
                                                    f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_phone}'
                                                    )
    btn_receiver_address = types.InlineKeyboardButton('Изменить адрес',
                                                      callback_data=
                                                      f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_address}'
                                                      )
    markup.row(btn_submit_info)
    markup.row(btn_receiver_name)
    markup.row(btn_receiver_phone)
    markup.row(btn_receiver_address)
    return markup


def create_edit_order_menu():
    markup = types.InlineKeyboardMarkup()
    btn_delivery_method = types.InlineKeyboardButton(text='Доставка',
                                                     callback_data=
                                                     f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_delivery}')
    btn_receiver_name = types.InlineKeyboardButton('ФИО',
                                                   callback_data=
                                                   f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_name}'
                                                   )

    btn_receiver_phone = types.InlineKeyboardButton('Телефон',
                                                    callback_data=
                                                    f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_phone}'
                                                    )
    btn_receiver_address = types.InlineKeyboardButton('Aдрес',
                                                    callback_data=
                                                    f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_receiver_address}'
                                                    )

    btn_cart = types.InlineKeyboardButton('Товары',
                                          callback_data=
                                          f'{TgUserAction.MARKER}{TgUserAction.edit_order}:{TgUserAction.edit_cart}')
    btn_cancel = types.InlineKeyboardButton('Оставить без изменений',
                                            callback_data=f'{TgUserAction.MARKER}{TgUserAction.submit_order_2}:order')

    markup.add(btn_delivery_method,
               btn_receiver_name,
               btn_receiver_phone,
               btn_receiver_address,
               btn_cart,
               btn_cancel,
               )

    return markup
