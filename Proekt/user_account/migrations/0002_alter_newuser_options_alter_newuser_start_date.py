# Generated by Django 4.1.1 on 2022-11-01 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 9, 26, 0, 495692, tzinfo=datetime.timezone.utc)),
        ),
    ]
