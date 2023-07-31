from django.contrib import admin
from .models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time', 'to_media')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_media')
