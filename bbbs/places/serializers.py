from rest_framework import serializers

from .models import Place, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = serializers.ALL_FIELDS     

    
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
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Place
        exclude = ("age", "gender", "activity_type", "show_on_main_page")

    def get_gender(self, obj):
        return obj.get_gender_display()


class PlacePostSerializer(serializers.ModelSerializer):
    tag = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Place
        exclude = ("show_on_main_page",)
