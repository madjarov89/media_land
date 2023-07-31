from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum
from django.core.validators import MinLengthValidator
from media_land.accounts.validators import only_letters_validator
from media_land.media.validators import validate_file_size


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    DO_NOT_SHOW = 3

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class MediaLandUser(AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            only_letters_validator
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.IntegerField(
        choices=Gender.choices(),
        default=3,
    )

    profile_picture = models.ImageField(
        validators=(validate_file_size,),
        upload_to="user_photos",
        blank=True,
        null=True)
