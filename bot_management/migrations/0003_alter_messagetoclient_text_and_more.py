# Generated by Django 4.2.5 on 2023-11-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_management', '0002_alter_messagetoclient_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetoclient',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='messagetoclient',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]