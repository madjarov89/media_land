from django.db import models
from django.core.validators import MinLengthValidator
from media_land.media.validators import validate_file_size
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Media(models.Model):
    image = models.ImageField(validators=(validate_file_size,),
                              upload_to="media",
                              blank=False,
                              null=False)

    link = models.URLField(
        blank=True,
        null=True
    )

    description = models.TextField(max_length=200,
                                   validators=(MinLengthValidator(10),),
                                   blank=True,
                                   null=True)

    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.media_image}"
