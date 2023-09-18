from rest_framework import serializers
from apps.home_page import models


class HeaderNavigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HeaderNavigation
        fields = "__all__"


class AdventageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adventage
        fields = "__all__"
