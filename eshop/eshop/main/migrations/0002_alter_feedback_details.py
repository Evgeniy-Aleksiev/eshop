# Generated by Django 4.0.4 on 2022-05-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='details',
            field=models.TextField(max_length=300),
        ),
    ]