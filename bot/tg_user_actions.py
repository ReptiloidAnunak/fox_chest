
from sales.models import Order, OrderStatus


def add_to_cart(bot_manager, product):
    order, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                 status=OrderStatus.CREATED)
    order.goods.add(product)
    order.save()


def delete_from_cart(bot_manager, product): # Команда выполняется только когда я нашимаю "/start". Надо ИСПРВИТЬ!
    order = Order.objects.filter(tg_user=bot_manager.tg_user).first()
    order.goods.remove(product)
    order.save()


class TgUserAction:
    MARKER = "act-"
    add_to_cart = 'add'
    add_to_favorite = 'favorite'
    delete_from_cart = 'delete'

    def __init__(self, action_call):
        self.action_data = action_call.split('-')
        self.action_code = self.action_data[1].split(':')[0]
        self.product_id = self.action_data[1].split(':')[1]

    def route(self, bot_manager, bot, chat_id):
        if self.action_code == self.add_to_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            add_to_cart(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в корзину! 🦊✅\nХотите оформить заказ или добавите что-то ещё?
                                            """)

        elif self.action_code == self.add_to_favorite:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в избранное! 🦊❤️\nВ любой момент вы можете посмотреть список заинтересовавших товаров с помощью команды /favorite в Меню
                                            """)

        elif self.action_code == self.delete_from_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            delete_from_cart(bot_manager, product)
            bot.send_message(chat_id, f"""Товар {product.name} удален из корзины! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)




