# Generated by Django 3.2.6 on 2021-10-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0023_auto_20210911_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='coalSignLocationWorld',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AddField(
            model_name='exchange',
            name='diamondSignLocationWorld',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AddField(
            model_name='exchange',
            name='goldSignLocationWorld',
            field=models.CharField(default='', max_length=260),
        ),
        migrations.AddField(
            model_name='exchange',
            name='ironSignLocationWorld',
            field=models.CharField(default='', max_length=260),
        ),
    ]
