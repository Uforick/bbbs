# Generated by Django 3.2.3 on 2021-05-23 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='common.city', verbose_name='Город'),
        ),
    ]
