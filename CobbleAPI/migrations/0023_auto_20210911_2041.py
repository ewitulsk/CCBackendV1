# Generated by Django 3.2.6 on 2021-09-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0022_auto_20210911_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='allowedCoalSigns',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='allowedDiamondSigns',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='allowedGoldSigns',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='allowedIronSigns',
            field=models.IntegerField(default=0),
        ),
    ]
