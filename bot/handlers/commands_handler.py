
from bot import messages
from bot.utils import check_tg_user, get_current_order
from bot.interface.interface_constructors import create_obj_menu_in_favorite, create_obj_menu_in_cart, create_order_menu, create_main_keyboard
from sales.models import Order, OrderStatus, Favorite


def route_commands(bot, message, bot_manager):
    command = message.text.lower()

    if command == '/start':
        check_tg_user(message, bot_manager)
        bot.send_message(message.chat.id,
                         text=messages.write_greetings(bot_manager),
                         reply_markup=create_main_keyboard()
                         )

    elif command == '/cart':
        chat_id = message.chat.id
        check_tg_user(message, bot_manager)
        get_current_order(bot_manager)
        cart, created = Order.objects.get_or_create(tg_user=bot_manager.tg_user,
                                                    status=OrderStatus.CREATED)

        goods = list(cart.goods.all())

        if not goods:
            bot.send_message(chat_id, text=messages.cart_is_empty)

        else:
            bot.send_message(chat_id, text="Ваша корзина 🛒")
            for obj in goods:
                bot.send_photo(chat_id, obj.image,
                               caption=messages.create_wear_obj_answer_txt(obj),
                               reply_markup=create_obj_menu_in_cart(obj, bot_manager))
            bot.send_message(chat_id, text="Хотите оформить заказ?", reply_markup=create_order_menu())

    elif command == '/favorite':
        chat_id = message.chat.id
        check_tg_user(message, bot_manager)
        fav_lst, created = Favorite.objects.get_or_create(tg_user=bot_manager.tg_user)

        goods = list(fav_lst.goods.all())

        if not goods:
            bot.send_message(chat_id, text="Ваш список избранного пуст")
        else:
            bot.send_message(chat_id, text="Ваши избранные товары: 🛒")
            for obj in goods:
                bot.send_photo(chat_id, obj.image,
                               caption=messages.create_wear_obj_answer_txt(obj),
                               reply_markup=create_obj_menu_in_favorite(obj, bot_manager))
