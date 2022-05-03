from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from eshop.core.validators import validate_only_letters

UserModel = get_user_model()


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 25

    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 3

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 3

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )