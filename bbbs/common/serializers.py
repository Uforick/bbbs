from django.shortcuts import get_object_or_404

from rest_framework import serializers

from bbbs.common.models import City, Profile


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = serializers.ALL_FIELDS


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = serializers.ALL_FIELDS

    def validate(self, attrs):
        profile = get_object_or_404(Profile, user=self.context['request'].user)
        cities = self.context['request'].data.getlist('city')
        if len(cities) > 1 and profile.is_mentor:
            raise serializers.ValidationError(
                {'FieldError': 'У наставника может быть только один город.'}
            )
        return attrs
