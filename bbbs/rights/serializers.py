from rest_framework import serializers

from bbbs.rights.models import Right


class RightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Right
        fields = "__all__"