# Generated by Django 5.1.2 on 2024-11-09 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_food", "0001_initial"),
        ("app_user", "0002_userinfo_is_worker"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("title", models.CharField(max_length=200)),
                ("title_info", models.CharField(max_length=400)),
                ("btn1", models.CharField(max_length=40)),
                ("btn1Link", models.CharField(max_length=40)),
                ("btn2", models.CharField(max_length=40)),
                ("btn2Link", models.CharField(max_length=40)),
            ],
        ),
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
                ("name", models.CharField(max_length=50)),
                ("menu_img", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("bookingEmail", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("logo", models.URLField()),
                (
                    "openHour",
                    models.CharField(
                        choices=[
                            ("Mon - Thu: 6pm - 11:30pm", "Mon - Thu: 6pm - 11:30pm"),
                            ("Fri - Sun: 8pm - 2am", "Fri - Sun: 8pm - 2pm"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Table",
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
                (
                    "table_no",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                        ],
                        max_length=2,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("booking_price", models.PositiveIntegerField()),
                ("is_booked", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="MenuList",
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
                ("item_name", models.CharField(max_length=100)),
                ("item_price", models.CharField(max_length=100)),
                ("ingredient1", models.CharField(max_length=100)),
                ("ingredient2", models.CharField(max_length=100)),
                ("ingredient3", models.CharField(max_length=100)),
                ("ingredient4", models.CharField(max_length=100)),
                ("is_recommended", models.BooleanField(default=False)),
                ("is_seasonal", models.BooleanField(default=False)),
                (
                    "menu",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menuList",
                        to="app_restuarent.menu",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("ordered_time", models.DateTimeField(auto_now_add=True)),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="app_food.food",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to="app_user.userinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("body", models.TextField()),
                (
                    "rating",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review",
                        to="app_user.userinfo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookTable",
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
                (
                    "num_persons",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "scheduled_time",
                    models.CharField(
                        choices=[
                            ("6:00pm - 6:30pm", "6:00pm - 6:30pm"),
                            ("6:30pm - 7:00pm", "6:30pm - 7:00pm"),
                            ("7:00pm - 7:30pm", "7:00pm - 7:30pm"),
                            ("7:30pm - 8:00pm", "7:30pm - 8:00pm"),
                            ("8:00pm - 8:30pm", "8:00pm - 8:30pm"),
                            ("8:30pm - 9:00pm", "8:30pm - 9:00pm"),
                            ("9:00pm - 9:30pm", "9:00pm - 9:30pm"),
                            ("9:30pm - 10:00pm", "9:30pm - 10:00pm"),
                            ("10:00pm - 10:30pm", "10:00pm - 10:30pm"),
                            ("10:30pm - 11:00pm", "10:30pm - 11:00pm"),
                            ("11:00pm - 11:30pm", "11:00pm - 11:30pm"),
                        ],
                        max_length=20,
                    ),
                ),
                ("scheduled_date", models.DateField()),
                ("booking_time", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="app_user.userinfo",
                    ),
                ),
                (
                    "table",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking",
                        to="app_restuarent.table",
                    ),
                ),
            ],
        ),
    ]