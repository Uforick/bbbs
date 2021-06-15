
from rest_framework.views import APIView
from rest_framework.response import Response

from bbbs.questions.models import Question
from bbbs.places.models import Place
from bbbs.rights.models import Right

from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer
from bbbs.rights.serializers import RightListSerializer



class MainView(APIView):

    def get(self,request):
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

        