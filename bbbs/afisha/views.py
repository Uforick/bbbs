from rest_framework import generics, status, permissions
from rest_framework.response import Response

from bbbs.afisha.models import Event
from bbbs.afisha.permissions import IsMentor
from bbbs.afisha.serializers import EventParticipantSerializer, EventSerializer
from bbbs.common.models import Profile


class EventList(generics.ListAPIView):
    queryset = Event.objects.all().order_by('start_at')
    serializer_class = EventSerializer
    pagination_class = None

    def get_queryset(self):
        events = None
        if self.request.user.is_superuser:
            events = Event.objects.all()
        elif self.request.user.is_authenticated:
            self_profile = generics.get_object_or_404(
                Profile, user=self.request.user)
            events = Event.objects.filter(
                city__in=self_profile.user_cities)
        elif not self.request.user.is_authenticated:
            events = Event.objects.filter(
                city=self.request.query_params.get('city'))

        return events


class EventParticipantList(generics.ListCreateAPIView,
                           generics.DestroyAPIView):

    serializer_class = EventParticipantSerializer
    permission_classes = [permissions.IsAuthenticated, IsMentor]

    def delete(self, request, *args, **kwargs):
        assert 'event' in request.data, 'Нет id события в запросе'
        event = request.data['event']
        object = self.get_queryset().filter(event=event)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        return self.request.user.event_user.all()
