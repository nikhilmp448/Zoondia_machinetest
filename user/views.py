from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import UserRegisterSerializer
from .serializers import UrlShortnerSerializer
from url.models import Url

# Create your views here.

class UserRegisterViewset(viewsets.ViewSet):

    def create(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)


class AdminViewset(viewsets.ViewSet):
    def list(self,request):
        value = Url.objects.all()
        data = UrlShortnerSerializer(value,many = True)
        return Response(data)









        

