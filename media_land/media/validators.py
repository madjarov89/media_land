from django.core.exceptions import ValidationError


def validate_file_size(image_obj):
    max_size = 5 * 1024 * 1024
    if image_obj.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
