# Generated by Django 4.0.5 on 2022-06-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
