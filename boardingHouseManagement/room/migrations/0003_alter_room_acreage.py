# Generated by Django 5.0.1 on 2024-03-15 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_rename_rooms_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='acreage',
            field=models.CharField(max_length=10),
        ),
    ]