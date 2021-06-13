from rest_framework import serializers

from .models import Place, Tag


class InfoField(serializers.Field):
    def to_representation(self, place):
        display = ""
        if place.gender:
            display += place.get_gender(place.gender) + ", "
        display += str(place.age) + " лет. "
        display += place.get_activity_type(place.activity_type) + " отдых"
        return display


class PlaceListSerializer(serializers.ModelSerializer):
    info = InfoField(source="*")

    class Meta:
        model = Place
        exclude = ("age", "gender", "activity_type", "tag",)

    def get_gender(self, obj):
        return obj.get_gender_display()


class PlacePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = serializers.ALL_FIELDS


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = serializers.ALL_FIELDS
