# Generated by Django 4.2.9 on 2024-02-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0003_remove_booking_booking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(max_length=5),
        ),
    ]
