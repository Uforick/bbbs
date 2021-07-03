from rest_framework import serializers

from bbbs.materials.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        exclude = ("show_on_main_page",)
