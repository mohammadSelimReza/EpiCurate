from django.db import models
from .validators import generate_random_key
from mptt.models import MPTTModel, TreeForeignKey
from app_user.models import UserInfo
from django.core.exceptions import ValidationError


class Category(MPTTModel):
    category_name = models.CharField(
        max_length=20, default="others", blank=True, null=True
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True, default="others"
    )

    class MPTTMeta:
        order_inserting_by = ["category_name"]

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=20, default="none", blank=True, null=True)

    def __str__(self):
        return self.brand_name


class Food(models.Model):
    idMeal = models.PositiveIntegerField(
        primary_key=True, default=generate_random_key, unique=True
    )
    strMeal = models.CharField(max_length=100)
    strCategory = TreeForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="foodCategory",
        blank=True,
        null=True,
        default="others",
    )
    strBrand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="foodBrand",
        blank=True,
        null=True,
        default="none",
    )
    strArea = models.CharField(max_length=50, blank=True, null=True)
    strMealThumb = models.URLField(blank=True, null=True)
    strDescription = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Custom validation: Only owners are allowed to add food
        if not self.added_by.is_owner:
            raise ValidationError("Only owners can add food items.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.strMeal


class Ingredient(models.Model):
    food = models.ForeignKey(Food, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # e.g., "2 cups"

    def __str__(self):
        return self.name
