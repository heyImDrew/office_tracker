# Generated by Django 3.1.2 on 2020-10-06 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0012_remove_booked_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='address',
        ),
        migrations.AddField(
            model_name='office',
            name='house',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='office',
            name='street',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='office',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
