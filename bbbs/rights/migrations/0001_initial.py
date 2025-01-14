# Generated by Django 3.2.3 on 2021-07-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RightTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тег')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('image', models.ImageField(blank=True, upload_to='rights/', verbose_name='Картинка')),
                ('show_on_main_page', models.BooleanField(default=False, verbose_name='Показать на главной странице')),
                ('tag', models.ManyToManyField(related_name='rights', to='rights.RightTag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Права ребенка',
                'verbose_name_plural': 'Права ребенка',
                'ordering': ('title',),
            },
        ),
    ]
