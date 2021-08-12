import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Question, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
        

class QuestionListSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    
    class Meta:
        model = Question
        exclude = ('show_on_main_page',)


class QuestionViewPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ('id', 'question')
   
    def validate_question(self, value):
        """
        Проверяем, что question это строка, а не число.
        """
        if re.match(r'[-+]?\d+?[\.\,]?\d+?', value):
            raise ValidationError(
                'Вопрос должен быть строкой!'
            )
        return value
