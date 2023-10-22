import typing

from bot.bot_manager import check_tg_user
from bot.interface.constructors import create_cat_wear_keyboard, create_wear_request_menu
from bot.interface.buttons import MainMenu, ChildWearMenu, SearchWearMenu
from bot.interface.menu_btns_functions import back_to_main_menu, back_to_wear_cat_menu
from bot.messages import WearPresentations, cart_is_empty
from bot.tg_user_actions import create_delivery_ways_menu
from bot.bot_manager import get_current_order
from sales.models import Order, OrderStatus

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
        print('e')
        # order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
        #                                                   status=OrderStatus.CREATED)
        accept_order_main_menu(bot, chat_id, bot_manager)


    # Выход
    elif message == SearchWearMenu.back_cat_menu.text:
        back_to_wear_cat_menu(bot, chat_id)


    elif message == ChildWearMenu.back.text:
        back_to_main_menu(bot, chat_id)



        return True
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