from telebot import TeleBot, types


class MainMenu:
    child_wear_btn = types.KeyboardButton("👕 Детская одежда ")
    macrame_doll_btn = types.KeyboardButton("🧶 Куклы макраме ")
    question = types.KeyboardButton("❓ Задать вопрос")


class ChildWearMenu:
    t_short = types.KeyboardButton("Майки")
    pants = types.KeyboardButton("Штаны")
    jacket = types.KeyboardButton("Куртки")
    bodysuit = types.KeyboardButton("Бодисвиты")


class TShortMenu:
    all_tshorts = types.KeyboardButton("Все майки")
    size_selection = types.KeyboardButton("Подобрать по размеру")
    color_selection = types.KeyboardButton("Подобрать по цвету")
    sex_selection = types.KeyboardButton("Подобрать для мальчика или девочки")
    brand_selection = types.KeyboardButton("Подобрать по бренду")
