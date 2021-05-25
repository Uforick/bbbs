from rest_framework import generics, permissions

from bbbs.afisha.models import Event, EventParticipant
from bbbs.afisha.serializers import EventSerializer, EventParticipantSerializer
from bbbs.common.models import Profile


class EventList(generics.ListAPIView):
    queryset = Event.objects.all().order_by('start_at')
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            events = Event.objects.all()
        elif self.request.user.is_authenticated:
            events = Event.objects.filter(Profile.city(self.request.user))
        elif self.request.user.is_anonymous:
            events = Event.objects.filter(city=self.kwargs.get('city'))
        return events



class EventParticipantList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer

