from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from bbbs.common.models import City

User = get_user_model()


class Event(models.Model):
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес',
        help_text='Укажите, место проведения события',
    )
    contact = models.CharField(
        max_length=200,
        verbose_name='Контакт',
        help_text='Укажите, контакт организатора события',
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Укажите, краткое описание предстоящего события',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Укажите, полное описание предстоящего события',
    )
    start_at = models.DateTimeField(
        verbose_name='Начало',
        help_text='Укажите, дату и время начала события',
    )
    end_at = models.DateTimeField(
        verbose_name='Окончание',
        help_text='Укажите, дату и время окончания события',
    )
    seats = models.PositiveIntegerField(
        verbose_name='Кол-во мест',
        help_text='Укажите, количество посадочных мест',
    )
    city = models.ForeignKey(
        City,
        verbose_name='Город',
        related_name='events',
        help_text='Укажите, наименование города проведения события',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    @property
    def taken_seats(self):
        return self.event_follow.count()

    @property
    def has_free_seats(self):
        return self.seats > self.taken_seats

    @property
    def has_started(self):
        return timezone.now() >= self.start_at

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ('city', '-start_at')


class EventParticipant(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='event_user',
        help_text='Выберите пользователя на предстоящее событие',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        verbose_name='Событие',
        related_name='event_follow',
        help_text='Выберите событие для пользователя',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.event.title

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ('user',)

        constraints = [
            models.UniqueConstraint(fields=['user', 'event'],
                                    name='unique_participation'),

        ]
