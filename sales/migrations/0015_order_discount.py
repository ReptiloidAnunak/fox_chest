# Generated by Django 4.2.5 on 2023-10-05 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0014_order_final_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.CharField(
                default="Нет", max_length=100, verbose_name="Скидка"
            ),
        ),
    ]
