# Generated by Django 5.1.2 on 2024-11-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_restuarent", "0005_rename_menu_foodmenu_rename_menulist_foodmenulist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="menu", max_length=50)),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        default="menu_slug",
                        max_length=100,
                        null=True,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]