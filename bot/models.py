from django.db import models

from core.models import User


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

    phone = models.CharField(max_length=30,
                                   null=True,
                                   verbose_name="Телефон")

    verification_code = models.CharField(max_length=20,
                                         null=True,
                                         verbose_name="Верифицационный код")



    def __str__(self):
        return f"""{self.username}"""








