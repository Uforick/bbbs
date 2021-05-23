from django.contrib.auth import get_user_model
from django.db import models
from bbbs.common.validators import city_name_validator


User = get_user_model()


class City(models.Model):
    name = models.CharField(
        verbose_name='Город',
        help_text='Введите название города',
        max_length=30,
        # Проверяем, что в названии города только русские буквы.
        validators=[city_name_validator],
        # Полагаю, что в нашем случае двух городов с одним названием - нет.
        unique=True
    )
    is_primary = models.BooleanField(
        # Возможно стоит дать другое название,но я так понял,
        # что это города выше черты см. ссылку
        # https://www.figma.com/file/11gCLSDOYlvkbuI3FU36Up/BBBS-for-students?node-id=1243%3A195
        verbose_name='Главный',
        help_text='Укажите главный ли город',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"
        # Сначала главные города, потом по алфавиту остальные
        ordering = ('-is_primary', 'name')


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        City,
        verbose_name='Город',
        null=True,
        blank=True,
        unique=False,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        # Сортируем по имени пользователя
        ordering = ('user__username',)
