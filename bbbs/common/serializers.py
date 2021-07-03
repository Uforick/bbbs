from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from bbbs.common.models import City, Profile




User = get_user_model()

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = serializers.ALL_FIELDS


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('role',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['city'] = data.get('city')[0]
        return data

    def validate(self, attrs):
        profile = get_object_or_404(Profile, user=self.context['request'].user)
        cities = self.context['request'].data.get('city')
        if cities is None:
            raise serializers.ValidationError(
                {'FieldError': 'Введите ID города в поле "city".'}
            )
        if len(cities) > 1 and profile.is_mentor:
            raise serializers.ValidationError(
                {'FieldError': 'У наставника может быть только один город.'}
            )
        return attrs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username, password = attrs.values()
        user_profile = Profile.objects.get(user__username = username)
        if not user_profile.is_mentor:
            error_message = "Получить токен можно только с ролью Наставник"
            raise exceptions.AuthenticationFailed(error_message)
        return super().validate(attrs)
