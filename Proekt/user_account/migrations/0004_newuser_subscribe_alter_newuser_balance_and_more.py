# Generated by Django 4.1.1 on 2022-11-02 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0003_newuser_balance_alter_newuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='subscribe',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='тип подписки'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='balance',
            field=models.PositiveBigIntegerField(default=0, verbose_name='баланс'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 7, 44, 23, 372433, tzinfo=datetime.timezone.utc)),
        ),
    ]