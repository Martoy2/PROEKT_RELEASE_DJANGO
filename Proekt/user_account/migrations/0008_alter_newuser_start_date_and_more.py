# Generated by Django 4.1.1 on 2022-11-25 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_alter_newuser_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 25, 16, 14, 48, 706220, tzinfo=datetime.timezone.utc), verbose_name='дата регистрации'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='subscribe_date',
            field=models.DateField(default=datetime.datetime(2022, 11, 25, 16, 14, 48, 706220, tzinfo=datetime.timezone.utc), verbose_name='подписка до'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='user_image',
            field=models.ImageField(default='user.png', upload_to='', verbose_name='фото профиля'),
        ),
    ]
