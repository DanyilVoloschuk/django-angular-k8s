from rest_framework import generics

from . import serializers
from . import models


class HeroListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.HeroListCreateSerializer
    queryset = models.Hero.objects.all()


class HeroRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.HeroRetrieveUpdateSerializer
    queryset = models.Hero.objects.all()
