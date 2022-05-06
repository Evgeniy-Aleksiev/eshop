from django.core.validators import MinLengthValidator
from django.db import models

from eshop.core.validators import validate_only_numbers


class Category(models.Model):
    ORAL_CARE = 'oral care'
    SKIN_CARE = 'skin care'
    SUN_CARE = 'sun care'
    HAIR_CARE = 'hair care'
    DECORATIVE_COSMETICS = 'decorative cosmetics'
    BODY_CARE = 'body care'
    PERFUMES = 'perfumes'

    ASSISTANT = [(x, x) for x in (ORAL_CARE, SKIN_CARE, SUN_CARE,
                                  HAIR_CARE, DECORATIVE_COSMETICS,
                                  BODY_CARE, PERFUMES)]

    product_type = models.CharField(
        max_length=max(len(x) for x, _ in ASSISTANT),
        choices=ASSISTANT,
    )

    class Meta:
        ordering = ('product_type', )


class Product(models.Model):
    PRODUCT_NAME_MAX_LEN = 100
    PRODUCT_NAME_MIN_LEN = 3

    LABEL_MAX_LEN = 50
    LABEL_MIN_LEN = 3

    TEXT_MAX_LENGTH = 300

    product_name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(PRODUCT_NAME_MIN_LEN),
        ),
    )

    product_label = models.CharField(
        max_length=LABEL_MAX_LEN,
        validators=(
            MinLengthValidator(LABEL_MIN_LEN),
        ),
    )

    product_image = models.ImageField()

    product_quantity = models.IntegerField(
        default=1,
        validators=(
            validate_only_numbers,
        )
    )

    product_price = models.FloatField(
        validators=(
            validate_only_numbers,
        ),
    )

    product_description = models.TextField(
        max_length=TEXT_MAX_LENGTH,
    )

    available = models.BooleanField(
        default=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
