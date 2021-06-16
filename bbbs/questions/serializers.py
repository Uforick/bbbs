from rest_framework import serializers

from .models import Question, Tag


class QuestionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ('verified',)


class QuestionViewPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')
