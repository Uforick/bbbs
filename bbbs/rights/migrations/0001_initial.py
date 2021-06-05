# Generated by Django 3.2.2 on 2021-06-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('color', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('tag', models.ManyToManyField(to='common.Tag')),
            ],
        ),
    ]
