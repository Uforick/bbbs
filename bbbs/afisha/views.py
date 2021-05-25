from rest_framework import generics

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
            self_profile = generics.get_object_or_404(Profile, user = self.request.user)
            events = Event.objects.filter(city = self_profile.get_city())
        elif self.request.user.is_anonymous:
            events = Event.objects.filter(city=self.kwargs.get('city'))
        return events



class EventParticipantList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = user.event_user.all()
        return queryset

    def get_object(self):
        obj = self.request.user.event_user.all()
        return obj
