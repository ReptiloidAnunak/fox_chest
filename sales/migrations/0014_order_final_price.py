# Generated by Django 4.2.5 on 2023-10-05 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0013_order_address_order_phone_receiver_order_receiver_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="final_price",
            field=models.IntegerField(default=0),
        ),
    ]