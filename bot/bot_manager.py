
from store.models import Wear, Brand, Doll
from bot.models import TgUser
from sales.models import Order, OrderStatus, OrderDolls


def get_brands_names_list():
    return list(Brand.objects.values_list('name', flat=True))


class BotManager:
    def __init__(self):
        self.tg_user: TgUser = None
        self.is_tg_user_new = False

        self.wear_cat: Wear = None
        self.all_brands_names = get_brands_names_list()

        self.doll_cat: Doll = None

        self.current_order = None
        self.order_total_price = 0

        self.current_order_dolls = None

        self.is_rec_info_submit = False


def check_tg_user(message, bot_manager: BotManager):
    tg_user_data = message.from_user
    tg_uid = tg_user_data.id
    obj, created = TgUser.objects.get_or_create(tg_user_id=tg_uid,
                                                  tg_chat_id=message.chat.id,
                                                  first_name=tg_user_data.first_name,
                                                  last_name=tg_user_data.last_name,
                                                  username=tg_user_data.username)
    bot_manager.tg_user = obj


def get_current_order(bot_manager: BotManager):
    current_order = Order.objects.filter(tg_user=bot_manager.tg_user,
                                         status=OrderStatus.CREATED).first()
    bot_manager.current_order = current_order
    return current_order


