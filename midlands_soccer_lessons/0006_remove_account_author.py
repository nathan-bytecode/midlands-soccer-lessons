# Generated by Django 4.2.9 on 2024-01-26 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0005_remove_booking_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='author',
        ),
    ]
