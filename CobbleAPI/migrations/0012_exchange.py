# Generated by Django 3.2.6 on 2021-08-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0011_auto_20210809_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('exFee', models.IntegerField(default=0)),
                ('coalSignOwner', models.CharField(max_length=20)),
                ('coalSignFee', models.IntegerField(default=0)),
                ('ironSignOwner', models.CharField(max_length=20)),
                ('ironSignFee', models.IntegerField(default=0)),
                ('goldSignOwner', models.CharField(max_length=20)),
                ('goldSignFee', models.IntegerField(default=0)),
                ('diamondSignOwner', models.CharField(max_length=20)),
                ('diamondSignFee', models.IntegerField(default=0)),
            ],
        ),
    ]
