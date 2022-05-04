from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_only_numbers(value):
    for num in value:
        if not num.isdigit():
            raise ValidationError('Value must contain only numbers')
