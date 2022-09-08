# Generated by Django 4.1.1 on 2022-09-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0005_alter_customers_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_code', models.CharField(max_length=8)),
                ('phone', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=32)),
                ('event_type', models.CharField(max_length=8)),
                ('status', models.BooleanField(default=False)),
                ('fk_room_code', models.CharField(max_length=8)),
                ('fk_customer_code', models.CharField(max_length=8)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=4)),
                ('capacity', models.IntegerField(default=7)),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
