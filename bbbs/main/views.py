from rest_framework.views import APIView
from rest_framework.response import Response

from bbbs.questions.models import Question
from bbbs.places.models import Place
from bbbs.rights.models import Right

from bbbs.afisha.serializers import EventSerializer
from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer
from bbbs.rights.serializers import RightSerializer

from bbbs.main.stubs import HISTORY, MOVIES, VIDEO, ARTICLES

DEFAULT_CITY = 'Москва'


class MainView(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            city = request.user.profile.city.first()
            events = city.events.all()
            places = city.place_set.filter(show_on_main_page=True)
        else:
            events = None
            places = Place.objects.filter(city__name=DEFAULT_CITY,
                                          show_on_main_page=True)

        questions = Question.objects.filter(show_on_main_page=True)
        rights = Right.objects.filter(show_on_main_page=True)

        questions_serializer = QuestionListSerializer(questions, many=True)
        places_serializer = PlaceListSerializer(places, many=True)
        events_serializer = EventSerializer(events, many=True,
                                            context={'request': request})
        rights_serializer = RightSerializer(rights, many=True)

        return Response({
            'event': events_serializer.data,
            'history': HISTORY,
            'place': places_serializer.data,
            'articles': ARTICLES,
            'movies': MOVIES,
            'video': VIDEO,
            'questions': questions_serializer.data,
            'rights': rights_serializer.data,
        })
