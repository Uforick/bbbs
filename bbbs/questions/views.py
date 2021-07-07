import re
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .filters import QuestionFilter
from .models import Question, Tag
from .serializers import (QuestionListSerializer,
                          QuestionViewPostSerializer,
                          TagSerializer)


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    filterset_class = QuestionFilter
    pagination_class = None

    def get_queryset(self):
        return super().get_queryset().filter(show_on_main_page=True)


class QuestionViewPost(generics.CreateAPIView,
                       generics.RetrieveAPIView,
                       generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionViewPostSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        id = self.request.data.get('id')
        if not id.isdigit():
            raise ValidationError(
                'Номер вопроса должен быть положительным целым числом!'
            )
        return get_object_or_404(Question, pk=id)


class QuestionTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
