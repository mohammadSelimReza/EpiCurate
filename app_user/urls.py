from rest_framework import routers
from .views import UserView, UserCreationView
from django.urls import include, path

router = routers.DefaultRouter()

router.register(r"list", UserView)
router.register(r"create", UserCreationView)

urlpatterns = [
    path("", include(router.urls)),
]
