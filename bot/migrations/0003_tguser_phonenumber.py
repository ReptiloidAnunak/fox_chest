# Generated by Django 4.2.5 on 2023-10-05 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0002_alter_tguser_first_name_alter_tguser_last_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="tguser",
            name="phonenumber",
            field=models.CharField(max_length=30, null=True, verbose_name="Телефон"),
        ),
    ]