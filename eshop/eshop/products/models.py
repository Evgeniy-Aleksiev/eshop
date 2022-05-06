from django.core.validators import MinLengthValidator
from django.db import models

from eshop.core.validators import validate_only_numbers


class Product(models.Model):
    PRODUCT_NAME_MAX_LEN = 100
    PRODUCT_NAME_MIN_LEN = 3

    oral care,\
         skin care, sun care, hair care, decorative cosmetics, body care and perfumes.

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(PRODUCT_NAME_MIN_LEN),
        ),
    )

    product_quantity = models.IntegerField(
        default=1,
        validators=(
            validate_only_numbers,
        )
    )

    product_type = models.CharField()
