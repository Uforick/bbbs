from rest_framework import serializers

from bbbs.rights.models import Right, RightTag


class RightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        exclude = ['show_on_main_page']


class RightTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RightTag
        fields = serializers.ALL_FIELDS
