# Generated by Django 5.0.2 on 2024-04-17 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0026_guests_checked_out_room_guests_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guests',
            old_name='checked_out_room',
            new_name='checkout',
        ),
    ]