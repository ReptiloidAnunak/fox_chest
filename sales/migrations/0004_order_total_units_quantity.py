# Generated by Django 4.2.5 on 2023-10-15 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_orderwearitem_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_units_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
