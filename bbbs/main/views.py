
from rest_framework.views import APIView
from rest_framework.response import Response

from bbbs.afisha.models import Event
from bbbs.questions.models import Question
from bbbs.places.models import Place
from bbbs.rights.models import Right

from bbbs.afisha.serializers import EventSerializer
from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer
from bbbs.rights.serializers import RightListSerializer



class MainView(APIView):

    def get(self,request):
        '''
        надо докрутить с Event моделью, плюс не ясно нужно ли
        verified в ней делать, вообще показалось что на встрече было одно,
        а потом в FAQ прочитал другое - 
        https://github.com/GasheK/bbbs/blob/master/docs/faq.md
        '''
        if request.user.is_authenticated:
            events = Event.objects.filter(verified=True)
        else:
            events = None
        questions = Question.objects.filter(verified=True)
        places = Place.objects.filter(verified=True)
        rights = Right.objects.filter(verified=True)
        questions_serializer = QuestionListSerializer(questions, many=True)
        places_serializer = PlaceListSerializer(places, many=True)
        rights_serializer = RightListSerializer(rights, many=True)
        return Response({
            'questions': questions_serializer.data,
            'places': places_serializer.data,
            'rights': rights_serializer.data,
        })

        