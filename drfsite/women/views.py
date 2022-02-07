from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women
from women.serialazers import WomenSerializer


class WomenApiView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})  # many значит читать все записи

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # проверяем на корректность введеные данные

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': WomenSerializer(post_new).data})  # преобразовывает объект в словарь


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerialazer
