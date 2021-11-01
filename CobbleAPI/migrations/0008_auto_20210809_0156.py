# Generated by Django 3.2.6 on 2021-08-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0007_remove_player_awaitingvalidation'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='mcsecret',
            field=models.CharField(default='null', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='mcusername',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
