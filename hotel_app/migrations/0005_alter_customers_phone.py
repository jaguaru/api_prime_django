# Generated by Django 4.1.1 on 2022-09-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0004_remove_room_hotel_delete_booking_delete_guest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
