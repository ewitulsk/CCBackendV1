# Generated by Django 3.2.6 on 2021-08-07 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0003_player_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='username',
            field=models.CharField(default='NA', max_length=150),
            preserve_default=False,
        ),
    ]