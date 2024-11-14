from django.contrib import admin
from .models import Menu, FoodMenu, FoodMenuList, Restaurant


# Register your models here.
# class MenuAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ["name", "slug"]

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(FoodMenu)
admin.site.register(FoodMenuList)
