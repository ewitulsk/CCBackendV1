# Generated by Django 3.2.6 on 2021-09-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0019_auto_20210911_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='coalSignOwner',
            field=models.CharField(default=models.CharField(max_length=20), max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='diamondSignOwner',
            field=models.CharField(default=models.CharField(max_length=20), max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='goldSignOwner',
            field=models.CharField(default=models.CharField(max_length=20), max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='ironSignOwner',
            field=models.CharField(default=models.CharField(max_length=20), max_length=20),
        ),
    ]
