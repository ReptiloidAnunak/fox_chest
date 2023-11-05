from telebot import types

from store import constants
from bot.tg_user_actions import TgUserAction


# Keyboards` buttons

class MainMenu:
    child_wear_cats = types.KeyboardButton("Детская одежда")
    macrame_doll = types.KeyboardButton("Куклы макраме")
    my_orders = types.KeyboardButton('Мои заказы')
    checkout_order = types.InlineKeyboardButton('Оформить заказ')
    question = types.KeyboardButton("❓ Задать вопрос")


class ChildWearMenu:
    t_short = types.KeyboardButton("Майки")
    pants = types.KeyboardButton("Штаны")
    jacket = types.KeyboardButton("Верхняя одежда")
    bodysuit = types.KeyboardButton("Боди, слипы")
    overall = types.KeyboardButton("Комбинезоны")
    clothing_set = types.KeyboardButton("Костюмы/комплекты")
    robe = types.KeyboardButton("Платья")
    long_sleeve = types.KeyboardButton("Лонгсливы")
    underwear = types.KeyboardButton("Нижнее белье")
    socks_tights = types.KeyboardButton("Носки/колготки")
    sweatshirt = types.KeyboardButton("Cвитшоты")
    back = types.KeyboardButton("Главное меню")


class SearchWearMenu:
    all = types.KeyboardButton("Все товары категории")
    size_selection = types.KeyboardButton("Подобрать по размеру")
    color_selection = types.KeyboardButton("Подобрать по цвету")
    sex_selection = types.KeyboardButton("Мальчик/девочка")
    brand_selection = types.KeyboardButton("Подобрать по бренду")
    back_cat_menu = types.KeyboardButton("Назад в категории одежды")
    back_main_menu = types.KeyboardButton("Главное меню")


class DollsMenu:
    all_dolls = types.KeyboardButton('Все куклы')
    angels = types.KeyboardButton('Ангелы')
    families = types.KeyboardButton('Семьи кукол')
    intividual = types.KeyboardButton('Индивидуальный заказ')


# Inline buttons

class WearSexChoice:
    MALE = types.InlineKeyboardButton(text="Мальчик",
                                      callback_data=constants.WearSex.MALE)
    FEMALE = types.InlineKeyboardButton(text="Девочка",
                                        callback_data=constants.WearSex.FEMALE)
    UNISEX = types.InlineKeyboardButton(text="Унисекс",
                                        callback_data=constants.WearSex.UNISEX)


class OrderMenu:
    my_cart = types.InlineKeyboardButton("Моя корзина", callback_data=f'{TgUserAction.MARKER}{TgUserAction.see_cart}:order')
    checkout_order = types.InlineKeyboardButton("Оформить заказ",
                                                callback_data=f'{TgUserAction.MARKER}{TgUserAction.checkout_order}:order')
    clear_cart = types.InlineKeyboardButton("Очистить корзину",
                                            callback_data=f'{TgUserAction.MARKER}{TgUserAction.empty_cart}:order')


class ContinueCheckoutOrder:
    continue_checkout = types.InlineKeyboardButton('Продложить', callback_data=f'{TgUserAction.MARKER}{TgUserAction.checkout_order}:order')