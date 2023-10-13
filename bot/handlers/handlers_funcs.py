

def check_availability(chat_id, bot, lst: list):
    if not lst:
        bot.send_message(chat_id, "Нет в наличии")
        return False
    else:
        return True

