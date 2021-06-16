from rest_framework import serializers

from bbbs.afisha.serializers import EventSerializer
from bbbs.questions.serializers import QuestionListSerializer
from bbbs.places.serializers import PlaceListSerializer
from bbbs.rights.serializers import RightListSerializer


class MainListSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)
    questions = QuestionListSerializer(many=True)
    places = PlaceListSerializer(many=True)
    rights = RightListSerializer(many=True)
