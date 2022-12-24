# Generated by Django 4.1.1 on 2022-11-02 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_newuser_subscribe_alter_newuser_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='subscribe_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 7, 52, 48, 147195, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 7, 52, 48, 147195, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='subscribe',
            field=models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('BASIC', 'BASIC'), ('PREMIUM', 'PREMIUM')], default='DEFAULT', max_length=7, verbose_name='тип подписки'),
        ),
    ]
