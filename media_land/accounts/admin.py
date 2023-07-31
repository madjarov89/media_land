from django.contrib import admin
from django.contrib.auth import get_user_model

User_Model = get_user_model()


@admin.register(User_Model)
class UserModelAdmin(admin.ModelAdmin):
    pass
