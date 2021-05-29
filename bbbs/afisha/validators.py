from django.core.exceptions import ValidationError
from rest_framework import serializers


class AvailableSeatsValidator:

    def __call__(self, value):
        assert 'event' in value, 'Нет id события в запросе'
        event = value['event']

        if not event.has_free_seats:
            message = 'К сожалению, свободных мест нет.'
            raise serializers.ValidationError(message)


class EventStartedValidator:

    def __call__(self, value):
        assert 'event' in value, 'Нет id события в запросе'
        event = value['event']

        if event.has_started:
            message = 'Событие уже началось.'
            raise serializers.ValidationError(message)


# class PositiveSeatsValueValidator:

#     def __call__(self, value):
#         if value <= 0:
#             message = 'Введите положительное число.'
#             raise ValidationError(message)

def positive_seats_value_validator(value):
    if value <= 0:
        message = 'Введите положительное число.'
        raise ValidationError(message)
        