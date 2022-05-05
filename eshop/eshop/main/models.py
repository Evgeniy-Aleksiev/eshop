from django.core.validators import MinLengthValidator
from django.db import models

from eshop.core.validators import validate_only_numbers


class ContactUs(models.Model):
    USER_MAX_LEN = 25
    USER_MIN_LEN = 3

    TEXT_MAX_LENGTH = 300

    name = models.CharField(
        max_length=USER_MAX_LEN,
        validators=(
            MinLengthValidator(USER_MIN_LEN),
        )
    )

    mobile_number = models.CharField(
        max_length=9,
        validators=(
            MinLengthValidator(8),
            validate_only_numbers,
        )
    )

    email = models.EmailField()

    message = models.TextField(
        max_length=TEXT_MAX_LENGTH,
    )

    date = models.DateField(
        auto_now_add=True,
    )
