# Generated by Django 3.2.6 on 2021-08-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CobbleAPI', '0004_player_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToValidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toValidate', models.TextField()),
            ],
        ),
    ]