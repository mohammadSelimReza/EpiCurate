from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r"food", views.FoodView)
router.register(r"category", views.CategoryView)
router.register(r"brand", views.BrandView)
router.register(r"ingredient", views.IngredientView)


urlpatterns = [
    path("api/", include(router.urls)),
]
