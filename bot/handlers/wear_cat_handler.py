from bot.interface.constructors import create_cat_wear_keyboard, create_wear_request_menu
from bot.interface.buttons import MainMenu, ChildWearMenu, SearchWearMenu
from bot.interface.menu_btns_functions import back_to_main_menu, back_to_wear_cat_menu

from bot.messages import WearPresentations
from bot.tg_user_acts_funcs import start_checkout_order
from bot.tg_user_actions import create_delivery_ways_menu
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

    elif message == SearchWearMenu.back_cat_menu.text:
        back_to_wear_cat_menu(bot, chat_id)

    elif message in [ChildWearMenu.back.text, SearchWearMenu.back_main_menu.text]:
        back_to_main_menu(bot, chat_id)
        return True
    else:
        return False


def accept_order(bot, chat_id, message, bot_manager):
    if message == MainMenu.checkout_order.text:
        start_checkout_order(bot_manager, bot, chat_id,
                             markup=create_delivery_ways_menu())
    else:
        return False
