from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER, USER_TYPE, USER_POSITION
from .validators import validate_nid, validate_phone_number, generate_random_key


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name="info", on_delete=models.CASCADE)
    id = models.PositiveIntegerField(
        primary_key=True, default=generate_random_key, unique=True
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    user_position = models.CharField(max_length=20, choices=USER_POSITION)
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER)
    phone = models.CharField(max_length=14, validators=[validate_phone_number])
    nid = models.CharField(max_length=10, validators=[validate_nid])
    street_address = models.TextField()
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=4)
    country = models.CharField(max_length=50)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Only required for managers and staff.",
        default=0,
    )

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Custom validation to enforce salary for managers/staff
        if self.user_type in ["manager", "staff"] and not self.salary:
            raise ValueError("Salary is required for managers and staff.")
        super().save(*args, **kwargs)
