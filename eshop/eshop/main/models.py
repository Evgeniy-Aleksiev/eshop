from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Feedback(models.Model):
    TEXT_MAX_LENGTH = 300

    details = models.TextField(
        max_length=TEXT_MAX_LENGTH,
    )

    date = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
