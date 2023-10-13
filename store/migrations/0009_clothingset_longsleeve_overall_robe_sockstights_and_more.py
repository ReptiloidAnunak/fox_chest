# Generated by Django 4.2.5 on 2023-10-08 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_wear_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClothingSet",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Костюм/комплект",
                "verbose_name_plural": "Костюмы/комплекты",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="LongSleeve",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лонгслив",
                "verbose_name_plural": "Лонгсливы",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="Overall",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комбинезон",
                "verbose_name_plural": "Комбинезоны",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="Robe",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платье",
                "verbose_name_plural": "Платья",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="SocksTights",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Носки/колготки",
                "verbose_name_plural": "Носки/колготки",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="Sweatshirt",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cвитшот",
                "verbose_name_plural": "Cвитшоты",
            },
            bases=("store.wear",),
        ),
        migrations.CreateModel(
            name="Underwear",
            fields=[
                (
                    "wear_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="store.wear",
                    ),
                ),
            ],
            options={
                "verbose_name": "Нижнее белье",
                "verbose_name_plural": "Нижнее белье",
            },
            bases=("store.wear",),
        ),
        migrations.AlterModelOptions(
            name="bodysuit",
            options={
                "verbose_name": "Боди, слип",
                "verbose_name_plural": "Боди, слипы",
            },
        ),
        migrations.AlterModelOptions(
            name="jacket",
            options={
                "verbose_name": "Верхняя одежда",
                "verbose_name_plural": "Верхняя одежда",
            },
        ),
        migrations.AlterModelOptions(
            name="pants",
            options={
                "verbose_name": "Штаны, джинсы",
                "verbose_name_plural": "Штаны, джинсы",
            },
        ),
    ]