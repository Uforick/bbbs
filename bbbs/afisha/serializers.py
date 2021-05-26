from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from bbbs.afisha.models import Event, EventParticipant

from bbbs.afisha.validators import (AvailableSeatsValidator,
                                    EventStartedValidator)


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        user = self.context.get('request').user
        return user.event_user.filter(event=obj).exists()

    class Meta:
        model = Event
        #  если через __all__, то нужно указать конкретно
        #  taken_seats = serializers.ReadOnlyField,
        #  но при этом нарушается порядок полей

        fields = ['id', 'booked', 'address', 'contact', 'title', 'description',
                  'start_at', 'end_at', 'seats', 'taken_seats', 'city']


class EventParticipantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EventParticipant
        fields = ['id', 'user', 'event']
        validators = [
            UniqueTogetherValidator(
                queryset=EventParticipant.objects.all(),
                fields=['user', 'event']
            ),
            AvailableSeatsValidator(),
            EventStartedValidator(),
        ]

