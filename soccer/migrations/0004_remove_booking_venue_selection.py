# Generated by Django 4.2.9 on 2024-01-26 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0003_alter_booking_venue_selection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='venue_selection',
        ),
    ]
