from django.db import models
from core.models import User
from store.models import Wear


class TgUser(models.Model):
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    tg_chat_id = models.IntegerField(verbose_name="ID чата")
    tg_user_id = models.IntegerField(unique=True, verbose_name="Телеграм-id")
    user = models.ForeignKey(User, null=True,
                             on_delete=models.CASCADE,
                             verbose_name="ID пользователя на сайте")
    first_name = models.CharField(max_length=150,
                                  null=True,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=150,
                                 null=True,
                                 verbose_name="Фамилия")
    username = models.CharField(max_length=150,
                                null=True,
                                verbose_name='Юзернейм в ТГ')
    verification_code = models.CharField(max_length=20,
                                         null=True,
                                         verbose_name="Верифицационный код")

    def __str__(self):
        return f"""{self.username}: {self.last_name} {self.first_name}"""


class TgUserAction:
    MARKER = "act-"
    add_to_cart = 'add'
    add_to_favorite = 'favorite'
    delete_from_cart = 'delete'

    def __init__(self, action_call):
        self.action_data = action_call.split('-')
        self.action_code = self.action_data[1].split(':')[0]
        self.product_id = self.action_data[1].split(':')[1]


    def route(self, bot_manager, bot, chat_id,):
        if self.action_code == self.add_to_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в корзину! 🦊✅\nХотите оформить заказ или добавите что-то ещё?
                                            """)
        elif self.action_code == self.add_to_favorite:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            bot.send_message(chat_id, f"""Товар {product.name} добавлен в избранное! 🦊❤️\nВ любой момент вы можете посмотреть список заинтересовавших товаров с помощью команды /favorite в Меню
                                            """)

        elif self.action_code == self.delete_from_cart:
            product = bot_manager.wear_cat.objects.get(id=self.product_id)
            bot.send_message(chat_id, f"""Товар {product.name} удален из корзины! 🦊❌️\n Воспользуйтесь Меню, если хотите посмотреть другие товары\n⬇️⬇️⬇️
                                            """)






