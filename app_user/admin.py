from django.contrib import admin
from .models import UserBioData, UserInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(UserBioData)
