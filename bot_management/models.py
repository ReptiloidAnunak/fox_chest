from django.db import models


class MessageToClient(models.Model):
    class Meta:
        verbose_name = 'Сообщение клиенту'
        verbose_name_plural = 'Сообщения клиенту'

    title = models.CharField(max_length=50, unique=True)
    text = models.CharField(max_length=500)
