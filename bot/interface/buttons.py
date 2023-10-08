from telebot import types

from store import constants
from bot.tg_user_actions import TgUserAction


# Keyboards` buttons

class MainMenu:
    child_wear_cats = types.KeyboardButton("Детская одежда")
    macrame_doll = types.KeyboardButton("Куклы макраме")
    question = types.KeyboardButton("❓ Задать вопрос")
    checkout_order = types.InlineKeyboardButton('Оформить заказ')


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
    back = types.KeyboardButton("Назад")

# Inline` buttons


class ChoiceWearMenu:
    all = types.InlineKeyboardButton("Все товары категории", callback_data="Все")
    size_selection = types.InlineKeyboardButton("Подобрать по размеру", callback_data="size")
    color_selection = types.InlineKeyboardButton("Подобрать по цвету", callback_data="color")
    sex_selection = types.InlineKeyboardButton("Мальчик/девочка", callback_data="sex")
    brand_selection = types.InlineKeyboardButton("Подобрать по бренду", callback_data="brand")


class WearSexChoice:
    MALE = types.InlineKeyboardButton(text="Мальчик",
                                      callback_data=constants.WearSex.MALE)
    FEMALE = types.InlineKeyboardButton(text="Девочка",
                                        callback_data=constants.WearSex.FEMALE)
    UNISEX = types.InlineKeyboardButton(text="Унисекс",
                                        callback_data=constants.WearSex.UNISEX)


class DollsMenu:
    all_dolls = types.KeyboardButton('Все куклы')
    angels = types.KeyboardButton('Ангелы')
    families = types.KeyboardButton('Семьи кукол')


class OrderMenu:
    my_cart = types.InlineKeyboardButton("Моя корзина", callback_data=f'{TgUserAction.MARKER}{TgUserAction.see_cart}:order')
    checkout_order = types.InlineKeyboardButton("Оформить заказ",
                                                callback_data=f'{TgUserAction.MARKER}{TgUserAction.checkout_order}:order')
    clear_cart = types.InlineKeyboardButton("Очистить корзину",
                                            callback_data=f'{TgUserAction.MARKER}{TgUserAction.empty_cart}:order')