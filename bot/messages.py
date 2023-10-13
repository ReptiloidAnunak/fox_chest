from bot.utils import BotManager
from store.models import Wear

unknown_command = 'Неизвестная команда'


def write_greetings(bot_manager: BotManager):
    greetings = f"""🦊Привет, {bot_manager.tg_user.first_name}!\n
    Я бот магазина детской одежды 'Лисий сундучок!'
    \nУ нас отличная коллекция детской одежды из Германии и Турции!
    \nТакже у нас есть куклы макраме, которые вы можете подарить как взрослым, так и детям!
    \n ⬇️ Выберите категорию ⬇️
    """
    return greetings


def create_wear_obj_txt(obj: Wear):

    obj_msg = (
                f"""
Товар: {obj.name}
Размер: {obj.size}
Цвет: {obj.color}
Материал: {obj.material}
Пол: {obj.sex}
Возраст: {obj.age}
Марка: {obj.brand}
В наличии: {obj.quantity} шт.
Цена: {obj.price}
Описание: {obj.description}
                """)
    return obj_msg


def create_wear_obj_txt_in_cart(obj: Wear):

    obj_msg = (
                f"""
Товар: {obj.name}
Размер: {obj.size}
Цвет: {obj.color}
Материал: {obj.material}
Пол: {obj.sex}
Возраст: {obj.age}
Марка: {obj.brand}
Количество: ???? шт.
Цена: {obj.price}
Описание: {obj.description}
                """)
    return obj_msg


class WearPresentations:
    tshort = 'Выберите майку'
    pants = 'Выберите штаны'
    jacket = 'Выберите куртку'
    bodysuit = 'Выберите бодисвит'
    overall = 'Выберите комбинезон'
    clothing_set = 'Выберите комплект'
    robe = 'Выберите платье'
    long_sleeve = 'Выберите лонгслив'
    underwear = 'Выберите нижнее белье'
    socks_tights = 'Выберите носки или колготки'
    sweatshirt = 'Выберите свитшот'


sex_choice = 'Для мальчика или девочки?'


cart_is_empty = ('Ваша корзина пуcтая! 🛒\n\n\n'
                 'Воспользуйтесь ⬇️ Меню ⬇️ или отправьте /start, чтобы найти интересующие товары и положить в корзину')


