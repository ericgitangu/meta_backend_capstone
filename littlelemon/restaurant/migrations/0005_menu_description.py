# Generated by Django 4.2 on 2024-02-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_booking_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
