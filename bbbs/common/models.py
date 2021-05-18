from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class City(models.Model):
    name = models.CharField(
        verbose_name= 'Город',
        help_text='Введите название города',
        max_length=30,
        unique=True
    )
    is_primary = models.BooleanField(
        verbose_name= 'Основной',
        help_text='Укажите, если город является основным для вас',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name= 'Пользователь', 
        on_delete=models.CASCADE)
    city = models.OneToOneField(City, 
        verbose_name= 'Город', 
        on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили'
        ordering = ('user',)