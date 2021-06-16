from random import choice

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from bbbs.afisha.models import Event
from bbbs.common.models import Profile
from bbbs.questions.models import Question
from bbbs.places.models import Place

from bbbs.afisha.serializers import EventSerializer
from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer


class MainView(APIView):

    def get(self, request):
        '''
        надо докрутить с Event моделью, плюс не ясно нужно ли
        verified в ней делать, вообще показалось что на встрече было одно,
        а потом в FAQ прочитал другое -
        https://github.com/GasheK/bbbs/blob/master/docs/faq.md
        '''
        if request.user.is_authenticated:
            user = get_object_or_404(Profile, user=self.request.user)
            event = list(
                Event.objects.filter(
                    city__name=user.user_cities[0]).values_list(
                        'pk',
                        flat=True
                    )
                )

            place = list(Place.objects.filter(
                city__name=user.user_cities[0],
                verified=True).values_list('pk', flat=True)
            )
        else:
            event = None  # Что-то вывести...
            # Может вынести самый главный город(Москва) в .env??
            place = Place.objects.filter(city__name='Москва', verified=True)

        if event:
            random_event = choice(event)
            event = Event.objects.get(pk=random_event)

        if place:
            random_place = choice(place)
            place = Place.objects.get(pk=random_place)
            print(place)

        questions = Question.objects.filter(verified=True)
        questions_serializer = QuestionListSerializer(questions, many=True)
        place_serializer = PlaceListSerializer(place)
        event_serializer = EventSerializer(event, many=True)

        return Response({
            'event': event_serializer.data,  # ЧТо-то не так, надо думать...
            'history': [],
            'place': place_serializer.data,
            'articles': [],  # 2
            'movies': [],  # 4
            'video': [],  # 1
            'questions': questions_serializer.data,  # не все, а несколько (доделать!)
        })
