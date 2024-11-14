from django.db import models
from app_food.models import Food
from app_user.models import UserInfo
from .constants import ONE_TO_TEN, AVAILABLE_TIME, OPEN_HOUR


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bookingEmail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    logo = models.URLField()
    openHour = models.CharField(choices=OPEN_HOUR, max_length=30)

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=200)
    title_info = models.CharField(max_length=400)
    bnr_img = models.URLField(default="none")
    btn1 = models.CharField(max_length=40)
    btn1Link = models.CharField(max_length=40)
    btn2 = models.CharField(max_length=40)
    btn2Link = models.CharField(max_length=40)

    def __str__(self):
        return self.id


class Menu(models.Model):
    name = models.CharField(max_length=50, default="menu")
    slug = models.SlugField(
        max_length=100, unique=True, blank=True, default="menu_slug"
    )

    def __str__(self):
        return self.name


class FoodMenu(models.Model):
    name = models.CharField(max_length=50)
    menu_img = models.URLField()

    def __str__(self):
        return self.name


class FoodMenuList(models.Model):
    menu = models.ForeignKey(
        FoodMenu, on_delete=models.CASCADE, related_name="menuList"
    )
    item_name = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    ingredient1 = models.CharField(max_length=100, blank=True, null=True)
    ingredient2 = models.CharField(max_length=100, blank=True, null=True)
    ingredient3 = models.CharField(max_length=100, blank=True, null=True)
    ingredient4 = models.CharField(max_length=100, blank=True, null=True)
    is_recommended = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name


class Review(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="review")
    body = models.TextField()
    rating = models.CharField(choices=ONE_TO_TEN, max_length=2, blank=True, null=True)

    def __str__(self):
        return f"Review by {self.user.username}"


class Table(models.Model):
    table_no = models.CharField(choices=ONE_TO_TEN, max_length=2)
    description = models.TextField(blank=True, null=True)
    booking_price = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.table_no}"


class BookTable(models.Model):
    user = models.ForeignKey(
        UserInfo, on_delete=models.CASCADE, related_name="bookings"
    )
    table = models.OneToOneField(
        Table, on_delete=models.CASCADE, related_name="booking"
    )
    num_persons = models.CharField(choices=ONE_TO_TEN, max_length=2)
    scheduled_time = models.CharField(choices=AVAILABLE_TIME, max_length=20)
    scheduled_date = models.DateField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user} for {self.table}"


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="orders")
    ordered_time = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order of {self.food} by {self.user}"
