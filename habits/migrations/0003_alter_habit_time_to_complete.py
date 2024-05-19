# Generated by Django 5.0.2 on 2024-05-19 11:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time_to_complete',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(120)], verbose_name='Время на выполнение'),
        ),
    ]