# Generated by Django 3.2.3 on 2021-05-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_alter_city_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='is_primary',
            field=models.BooleanField(default=False, help_text='Укажите главный ли город', verbose_name='Главный'),
        ),
    ]
