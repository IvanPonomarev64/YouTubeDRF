from rest_framework import generics
from django.shortcuts import render
from women.models import Women
from women.serialazers import WomenSerialazer


class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerialazer
