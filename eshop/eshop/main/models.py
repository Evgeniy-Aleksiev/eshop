from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Feedback(models.Model):
    email = models.EmailField()

    details = models.TextField()

    date = models.DateField(
        auto_now_add=True,
    )

    user_feedback = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )