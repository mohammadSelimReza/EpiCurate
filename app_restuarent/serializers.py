from rest_framework import serializers
from . import models


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = [
            "name",
            "email",
            "bookingEmail",
            "phone",
            "address",
            "logo",
            "openHour",
        ]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ["name", "slug"]


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = [
            "title",
            "title_info",
            "btn1",
            "btn1Link",
            "btn2",
            "btn2Link",
            "bnr_img",
        ]


class FoodMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FoodMenu
        fields = ["name", "menu_img"]


class FoodMenuListSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.FoodMenuList
        fields = [
            "menu",
            "name",
            "item_name",
            "item_price",
            "ingredient1",
            "ingredient2",
            "ingredient3",
            "ingredient4",
            "is_recommended",
            "is_seasonal",
        ]

    def get_name(self, obj):
        return obj.menu.name

    # def create(self, validated_data):
    #     menu_data = validated_data.pop("menu")
    #     menu = MenuSerializer.create(MenuSerializer(), validated_data=menu_data)

    #     menu_list = models.MenuList.objects.create(
    #         menu=menu,
    #         item_name=validated_data.get("item_name"),
    #         item_price=validated_data.get("item_price"),
    #         ingredient1=validated_data.get("ingredient1"),
    #         ingredient2=validated_data.get("ingredient2"),
    #         ingredient3=validated_data.get("ingredient3"),
    #         ingredient4=validated_data.get("ingredient4"),
    #     )

    #     return menu_list


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = [
            "body",
            "rating",
        ]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Table
        fields = [
            "table_no",
            "description",
            "booking_price",
            "is_booked",
        ]


class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookTable
        fields = [
            "user",
            "table",
            "num_persons",
            "scheduled_time",
            "scheduled_date",
            "booking_time",
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            "food",
            "user",
            "ordered_time",
            "quantity",
        ]
