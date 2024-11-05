from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()


router.register(r"users", views.UserCreationView)

urlpatterns = [
    path("", include(router.urls)),
    # path("users/", views.UserCreationView),
]
