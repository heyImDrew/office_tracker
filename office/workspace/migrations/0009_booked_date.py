# Generated by Django 3.1.2 on 2020-10-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0008_auto_20201003_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
