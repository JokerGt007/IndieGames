# Generated by Django 5.0.7 on 2024-08-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_game_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='linkimage',
            field=models.CharField(default='https://store.steampowered.com/', max_length=100),
        ),
    ]
