from django.shortcuts import get_object_or_404
from rest_framework import generics

from .filters import QuestionFilter
from .models import Question, Tag
from .serializers import (QuestionListSerializer,
                          QuestionViewPostSerializer,
                          TagSerializer)


class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    filterset_class = QuestionFilter

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(verified=True)


class QuestionViewPost(generics.CreateAPIView,
                       generics.RetrieveAPIView,
                       generics.UpdateAPIView,
                       generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionViewPostSerializer
    
    def get_object(self):
        id = self.request.query_params.get('id')
        return get_object_or_404(Question, pk=id)

        
class QuestionTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
