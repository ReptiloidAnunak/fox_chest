from bot.interface.interface_constructors import create_wear_request_menu
from bot.interface.buttons import MainMenu, ChildWearMenu
from bot.messages import WearPresentations
from bot.tg_user_acts_funcs import start_checkout_order
from bot.tg_user_actions import create_delivery_ways_menu
from store import models as wear_models


def handle_wear_cat_request(bot, chat_id, message, bot_manager):
    if message == ChildWearMenu.t_short.text:
        bot_manager.wear_cat = wear_models.TShort
        create_wear_request_menu(bot=bot, message=message,
                                 chat_id=chat_id,
                                 msg_text=WearPresentations.tshort_presentation)

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
        return True
    else:
        return False


def accept_order(bot, chat_id, message, bot_manager):
    if message == MainMenu.checkout_order.text:
        start_checkout_order(bot_manager, bot, chat_id,
                             markup=create_delivery_ways_menu())
    else:
        return False
