# Generated by Django 4.2.5 on 2023-10-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0007_alter_wear_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="wear",
            name="quantity",
            field=models.IntegerField(default=0, null=True, verbose_name="Количество"),
        ),
    ]
