from django.contrib import admin
from .models import Category, Brand, Food

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Food)
