import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerialazer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel('Bibi', 'Cool')
    model_sr = WomenSerialazer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)  # преобразуем в байтовую json строку
    print(json)


def decode():
    stream = io.BytesIO(b'{"title":"Bibi","content":"Cool"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerialazer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
