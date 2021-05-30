# Generated by Django 3.2.3 on 2021-05-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_alter_profile_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('user__username',), 'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'администратор'), ('MODERATOR', 'модератор'), ('REGION_MODERATOR', 'региональный модератор'), ('MENTOR', 'наставник')], default='MENTOR', max_length=30, verbose_name='Роль'),
        ),
    ]
