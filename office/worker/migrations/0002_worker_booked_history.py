# Generated by Django 3.1.2 on 2020-10-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='booked_history',
            field=models.ManyToManyField(to='workspace.Booked'),
        ),
    ]