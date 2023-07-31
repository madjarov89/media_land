from django.contrib import admin
from .models import Media


@admin.register(Media)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "date_of_publication", "description",)
