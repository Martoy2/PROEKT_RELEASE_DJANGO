# Generated by Django 4.1.1 on 2022-12-20 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0019_course_alter_newuser_start_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkpayment',
            options={'verbose_name': 'Платеж', 'verbose_name_plural': 'Платежи'},
        ),
        migrations.AddField(
            model_name='course',
            name='subscribe_type',
            field=models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('BASIC', 'BASIC'), ('PREMIUM', 'PREMIUM')], default='DEFAULT', max_length=7, verbose_name='тип подписки'),
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 14, 39, 47, 545137, tzinfo=datetime.timezone.utc), verbose_name='дата курса'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 14, 39, 47, 544137, tzinfo=datetime.timezone.utc), verbose_name='дата регистрации'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='subscribe_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 14, 39, 47, 544137, tzinfo=datetime.timezone.utc), verbose_name='подписка до'),
        ),
    ]
