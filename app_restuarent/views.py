from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.
class RestaurantView(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class BannerView(viewsets.ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class MenuView(viewsets.ModelViewSet):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer


class MenuListView(viewsets.ModelViewSet):
    queryset = models.MenuList.objects.all()
    serializer_class = serializers.MenuListSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer


class TableView(viewsets.ModelViewSet):
    queryset = models.Table.objects.all()
    serializer_class = serializers.TableSerializer


class BookTableView(viewsets.ModelViewSet):
    queryset = models.BookTable.objects.all()
    serializer_class = serializers.BookTableSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
