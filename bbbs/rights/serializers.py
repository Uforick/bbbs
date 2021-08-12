from rest_framework import serializers

from bbbs.rights.models import Right, Tag


class RightTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = serializers.ALL_FIELDS

class RightSerializer(serializers.ModelSerializer):
    tag = RightTagSerializer(read_only=True, many=True)

    class Meta:
        model = Right
        exclude = ['show_on_main_page']

