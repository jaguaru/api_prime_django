# Generated by Django 4.1.1 on 2022-09-08 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0003_alter_customers_phone_alter_rooms_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
