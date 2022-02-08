from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from women.models import Women
from women.serialazers import WomenSerializer


# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})  # many значит читать все записи
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)  # проверяем на корректность введеные данные
#         serializer.save()
#         return Response({'post': serializer.data})  # преобразовывает объект в словарь
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT hot allowed"})
#         try:
#             isinstance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=isinstance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE hot allowed"})
#         try:
#             Women.objects.get(pk=pk).delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({'post': "delete post - " + str(pk)})


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
