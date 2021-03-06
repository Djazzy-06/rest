# Generated by Django 4.0.5 on 2022-07-01 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='addres',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.AddField(
            model_name='orders',
            name='table',
            field=models.EmailField(default=None, max_length=100, verbose_name='Столик'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 1, 15, 36, 22, 218330), verbose_name='Дата'),
        ),
    ]
