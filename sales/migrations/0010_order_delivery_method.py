# Generated by Django 4.2.5 on 2023-10-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0009_alter_favorite_tg_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="delivery_method",
            field=models.CharField(
                choices=[
                    ("Почта России", "Почта России"),
                    ("Boxberry", "Boxberry"),
                    ("CДЭК", "CДЭК"),
                    ("Авито", "Авито"),
                ],
                default="Неизвестно",
                max_length=20,
                verbose_name="Способ доставки",
            ),
        ),
    ]