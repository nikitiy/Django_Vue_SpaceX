from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.home_page import models
from . import serializers


def homePage(request):
    return render(request, "home_page/home_page.html")


class HeaderNavigationViewSet(ReadOnlyModelViewSet):
    queryset = models.HeaderNavigation.objects.all()
    serializer_class = serializers.HeaderNavigationSerializer


class AdventageViewSet(ReadOnlyModelViewSet):
    queryset = models.Adventage.objects.all()
    serializer_class = serializers.AdventageSerializer
