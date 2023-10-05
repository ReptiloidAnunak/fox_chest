from bot.utils import BotManager, create_wear_request_menu
from store import models as wear_models

unknown_command = 'Неизвестная команда'


def write_greetings(bot_manager: BotManager):
    greetings = f"""🦊Привет, {bot_manager.tg_user.first_name}!\n
    Я бот магазина детской одежды 'Лисий сундучок!'
    \nУ нас отличная коллекция детской одежды из Германии и Турции!
    \nТакже у нас есть куклы макраме, которые вы можете подарить как взрослым, так и детям!
    \n ⬇️ Выберите категорию ⬇️
    """
    return greetings


class WearPresentations:
    tshort_presentation = 'Выберите майку'
    pants_presentation = 'Выберите штаны'
    jacket_presentation = 'Выберите куртку'
    bodysuit_presentation = 'Выберите бодисвит'


sex_choice = 'Для мальчика или девочки?'





