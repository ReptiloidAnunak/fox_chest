from bot.utils import BotManager


def write_greetings(bot_manager: BotManager):
    greetings = f"""🦊Привет, {bot_manager.tg_user.first_name}!\n
    Я бот магазина детской одежды 'Лисий сундучок!'
    \nУ нас отличная коллекция детской одежды из Германии и Турции!
    \nТакже у нас есть куклы макраме, которые вы можете подарить как взрослым, так и детям!
    \n ⬇️ Выберите категорию ⬇️
    """
    return greetings


wear_presentation = """\nВыберите категорию"""

tshort_presentation = "Выберите майку"

unknown_command = 'Неизвестная команда'

sex_choice = 'Для мальчика или девочки?'

