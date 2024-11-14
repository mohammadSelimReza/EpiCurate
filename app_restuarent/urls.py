from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register(r"res", views.RestaurantView, basename="res_manage")
router.register(r"banner", views.BannerView, basename="banner_manage")
router.register(r"foodMenu", views.MenuView, basename="menu_manage")
router.register(r"foodMenuList", views.MenuListView, basename="menu_list_manage")
router.register(r"review", views.ReviewView, basename="review_manage")
router.register(r"table", views.TableView, basename="table_manage")
router.register(r"booking", views.BookTableView, basename="booking_manage")
router.register(r"order", views.OrderView, basename="order_manage")
router.register(r"menu", views.MenuViewSet, basename="menuLink")

urlpatterns = [
    path("", include(router.urls)),
]
