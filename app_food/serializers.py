from rest_framework import serializers
from .models import Category, Food, Ingredient, Brand


class CategorySerializer(serializers.ModelSerializer):
    parent_name = serializers.CharField(source="parent.category_name", read_only=True)

    class Meta:
        model = Category
        fields = ["id", "category_name", "parent", "parent_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name"]


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"
