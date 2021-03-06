# Generated by Django 4.0.4 on 2022-05-05 12:01

import django.core.validators
from django.db import migrations, models
import eshop.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3)])),
                ('mobile_number', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8), eshop.core.validators.validate_only_numbers])),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
