# Generated by Django 4.2.5 on 2023-10-05 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0002_alter_tguser_first_name_alter_tguser_last_name_and_more"),
        ("sales", "0008_alter_favorite_tg_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="tg_user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="bot.tguser",
                verbose_name="Пользователь Телеграм",
            ),
        ),
    ]
