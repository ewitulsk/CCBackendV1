# Generated by Django 3.2.6 on 2021-08-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0012_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='registeree',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='coalSignOwner',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='diamondSignOwner',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='goldSignOwner',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='exchange',
            name='ironSignOwner',
            field=models.CharField(default='', max_length=20),
        ),
    ]
