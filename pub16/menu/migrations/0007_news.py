# Generated by Django 4.0.5 on 2022-06-10 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_dish_calories_alter_dish_compound_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
    ]
