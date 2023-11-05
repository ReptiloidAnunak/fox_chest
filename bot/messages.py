from bot.bot_manager import BotManager
from bot.constants import MIN_INTERVAL_AFTER_CART_UPT, MAIN_TG_CONTACT, TEC_SUPPORT_CONTACT
from store.models import Wear
from sales.models import OrderWearItem

unknown_command = 'Неизвестная команда'

contact_message = (f'По поводу заказов и качества работы менеджеров пишите Ольге {MAIN_TG_CONTACT}'
                   f'\n\nЕсли вы обранужили проблему в работе бота, пишите в техподдержку 🛠 : {TEC_SUPPORT_CONTACT}'
                   f'\nПо возможности сопропровождайте сообщения об ошибках скриншотами'
                   f'\n\nМы будем благодарны за ваши отзывы! Благодаря Вам мы становимся лучше !🦊👍🏻'
                   )


doll_individual_message = (f'Напишите Ольге и подробно опишите, какая композиция кукол макраме вам нужна'
                           f'\n{MAIN_TG_CONTACT}')

def write_greetings(bot_manager: BotManager):
    greetings = f"""
    🦊Привет, {bot_manager.tg_user.first_name}!
    \nЯ бот магазина детской одежды 'Лисий сундучок!'
    \nУ нас отличная коллекция детской одежды из\nГермании 🇩🇪 и Турции 🇹🇷!
    \nТовары в вашей корзине гарантированно сохранятся в течение {MIN_INTERVAL_AFTER_CART_UPT} мин., поэтому не забудьте оформить заказ до конца!
    ☝🏾🦊⏰
    \n ⬇️ Выберите категорию ⬇️
    """
    # \nТакже у нас есть куклы макраме, которые вы можете подарить как взрослым, так и детям!
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


def create_wear_obj_txt_in_cart(obj: Wear, order):
    item_in_cart = OrderWearItem.objects.filter(order=order,
                                                wear=obj).first()

    obj_msg = (
                f"""
Товар: {obj.name}
Размер: {obj.size}
Цвет: {obj.color}
Материал: {obj.material}
Пол: {obj.sex}
Возраст: {obj.age}
Марка: {obj.brand}
Цена за 1 шт.: {obj.price} 
Количество: {item_in_cart.quantity} - {item_in_cart.total_price} р.
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


