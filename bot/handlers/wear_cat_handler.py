
from bot.interface.constructors import create_cat_wear_keyboard, create_wear_request_menu, create_dolls_menu
from bot.interface.buttons import MainMenu, ChildWearMenu, SearchWearMenu, DollsMenu
from bot.interface.menu_btns_functions import back_to_main_menu, back_to_wear_cat_menu
from bot.messages import WearPresentations, cart_is_empty, contact_message
from bot.tg_user_actions import create_delivery_ways_menu
from sales.models import OrderWearItem
from sales.models import Order
from sales.constants import OrderStatus
from store import models as wear_models


def handle_wear_cat_request(bot, chat_id, message, bot_manager):

    if message == MainMenu.child_wear_cats.text:
        create_cat_wear_keyboard(bot,
                                 chat_id,
                                 msg_text='Выберите категорию')

    elif message == ChildWearMenu.t_short.text:
        bot_manager.wear_cat = wear_models.TShort
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.tshort)

    elif message == ChildWearMenu.pants.text:
        bot_manager.wear_cat = wear_models.Pants
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.pants)

    elif message == ChildWearMenu.jacket.text:
        bot_manager.wear_cat = wear_models.Jacket
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.jacket)

    elif message == ChildWearMenu.bodysuit.text:
        bot_manager.wear_cat = wear_models.Bodysuit
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.bodysuit)

    elif message == ChildWearMenu.overall.text:
        bot_manager.wear_cat = wear_models.Overall
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.overall)

    elif message == ChildWearMenu.clothing_set.text:
        bot_manager.wear_cat = wear_models.ClothingSet
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.clothing_set)

    elif message == ChildWearMenu.robe.text:
        bot_manager.wear_cat = wear_models.Robe
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.robe)

    elif message == ChildWearMenu.long_sleeve.text:
        bot_manager.wear_cat = wear_models.LongSleeve
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.long_sleeve)

    elif message == ChildWearMenu.underwear.text:
        bot_manager.wear_cat = wear_models.Underwear
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.underwear)

    elif message == ChildWearMenu.socks_tights.text:
        bot_manager.wear_cat = wear_models.SocksTights
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.socks_tights)

    elif message == ChildWearMenu.sweatshirt.text:
        bot_manager.wear_cat = wear_models.Sweatshirt
        create_wear_request_menu(bot=bot,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.sweatshirt)

    elif message == MainMenu.checkout_order.text:
        accept_order_main_menu(bot, chat_id, bot_manager)


    # Выход
    elif message == SearchWearMenu.back_cat_menu.text:
        back_to_wear_cat_menu(bot, chat_id)

    # Назад
    elif message == ChildWearMenu.back.text:
        back_to_main_menu(bot, chat_id)

    # Текущие заказы
    elif message == MainMenu.my_orders.text:
        orders = Order.objects.filter(tg_user=bot_manager.tg_user).exclude(status=OrderStatus.CREATED).order_by('status')
        # print(orders)
        if orders:
            bot.send_message(chat_id, text='Ваши заказы:')
            for order in orders:
                goods = OrderWearItem.objects.filter(order=order)
                print(goods)
                goods_lst_msg = []
                for item in goods:
                    goods_lst_msg.append(item.create_str_in_my_ord_msg())
                goods_lst = ", ".join(goods_lst_msg)
                print(goods_lst)

                bot.send_message(chat_id, text=
                    f'\nЗаказ № {order.id}'
                    f'\n\nСтатус: {order.status}'
                    f'\n\nДата оформления: {order.created.strftime("%Y-%m-%d")}'
                    f'\nСпособ доставки: {order.delivery_method}'
                    f'\nАдрес доставки: {order.address}'
                    f'\nПолучатель: {order.receiver}'
                    f'\nТелефон получателя: {order.phone_receiver}'
                    f'\nТовары: {goods_lst}'
                    f'\nВсего: {order.final_price} p.')
            return True
        else:
            bot.send_message(chat_id, text='У вас нет оформленных заказов')

    # Вопрос
    elif message == MainMenu.question.text:
        bot.send_message(chat_id, text=contact_message)
        return True

    # Куклы
    elif message == MainMenu.macrame_doll.text:
        create_dolls_menu(bot, chat_id)
        return True

    elif message == DollsMenu.all_dolls.text:
        dolls = wear_models.Doll.objects.all()
        for doll in dolls:
            bot.send_photo(chat_id, doll.image, caption=doll.create_card_in_catalog())

    elif message == DollsMenu.angels.text:
        angels = wear_models.Angel.objects.all()
        for angel in angels:
            bot.send_photo(chat_id, angel.image, caption=angel.create_card_in_catalog())

    elif message == DollsMenu.families.text:
        families = wear_models.Family.objects.all()
        for family in families:
            bot.send_photo(chat_id, family.image, caption=family.create_card_in_catalog())
    else:
        return False


def accept_order_main_menu(bot, chat_id, bot_manager):
    order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                              status=OrderStatus.CREATED)
    goods = list(order.goods.all())
    if not goods:
        bot.send_message(chat_id, text=cart_is_empty)
    else:
        bot.send_message(chat_id, text=order.create_final_order_msg(),
                         reply_markup=create_delivery_ways_menu())

    return True