from rest_framework import serializers

from bbbs.afisha.models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = serializers.ALL_FIELDS


class EventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = ['id', 'event']
