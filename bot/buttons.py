from telebot import types


class MainMenu:
    child_wear_btn = types.KeyboardButton("👕 Детская одежда ")
    macrame_doll_btn = types.KeyboardButton("🧶 Куклы макраме ")
    question = types.KeyboardButton("❓ Задать вопрос")


class ChildWearMenu:
    t_short = types.KeyboardButton("Майки")
    pants = types.KeyboardButton("Штаны")
    jacket = types.KeyboardButton("Куртки")
    bodysuit = types.KeyboardButton("Бодисвиты")


class WearMenu:
    all = types.InlineKeyboardButton("Все товары категории", callback_data="Все")
    size_selection = types.InlineKeyboardButton("Подобрать по размеру", callback_data="size")
    color_selection = types.InlineKeyboardButton("Подобрать по цвету", callback_data="color")
    sex_selection = types.InlineKeyboardButton("Подобрать для мальчика или девочки", callback_data="sex")
    brand_selection = types.InlineKeyboardButton("Подобрать по бренду", callback_data="brand")
