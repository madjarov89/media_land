from django.db import models
from media_land.media.models import Media
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Comment(models.Model):
    # Required
    comment_text = models.TextField(max_length=200, blank=False, null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    to_media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return f"{self.date_time} {self.to_media}"


class Like(models.Model):
    to_media = models.ForeignKey(Media, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.to_media}"


class Search(models.Model):
    search_text = models.CharField(max_length=100, blank=False, null=False)
