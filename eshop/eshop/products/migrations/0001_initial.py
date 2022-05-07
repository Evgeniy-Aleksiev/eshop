# Generated by Django 4.0.4 on 2022-05-07 17:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import eshop.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('oral care', 'oral care'), ('skin care', 'skin care'), ('sun care', 'sun care'), ('hair care', 'hair care'), ('decorative cosmetics', 'decorative cosmetics'), ('body care', 'body care'), ('perfumes', 'perfumes')], max_length=20)),
            ],
            options={
                'ordering': ('product_type',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('product_label', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('product_image', models.ImageField(upload_to='')),
                ('product_quantity', models.IntegerField(default=1, validators=[eshop.core.validators.validate_only_numbers])),
                ('product_price', models.FloatField(validators=[eshop.core.validators.validate_only_numbers])),
                ('product_description', models.TextField(max_length=300)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
