from django.shortcuts import render
from .models import Ingredient, Food, Category, Brand
from .serializers import (
    CategorySerializer,
    FoodSerializer,
    IngredientSerializer,
    BrandSerializer,
)
from rest_framework import viewsets, response


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
