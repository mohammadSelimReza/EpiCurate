from django.db import models
from django.contrib.auth.models import User
from .constants import USER_TYPE, USER_POSITION, GENDER
from .validators import generate_random_key, validate_nid, validate_phone_number


# Create your models here.
class UserBioData(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    id = models.PositiveIntegerField(
        primary_key=True, default=generate_random_key, unique=True
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    user_position = models.CharField(max_length=20, choices=USER_POSITION)
    is_owner = False
    is_manager = False
    is_customer = False

    def __str__(self):
        return self.user.username


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="info")
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=14, validators=[validate_phone_number])
    nid = models.CharField(max_length=10, validators=[validate_nid])
    street_address = models.TextField()
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=4)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username
