from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UrlShortnerSerializer
import random
from . models import Url
from string import ascii_lowercase
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from django.db.models import F


def generate_random_urlskey(length=15):
    return 'http://127.0.0.1:8000/url/'.join(random.choice(ascii_lowercase)for _ in range(length))


class Urlviewset(viewsets.ViewSet):
    parser_classes = [JSONParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        data = Url.objects.filter(shortend_url = pk)
        return Response(data)
    
    def list(self,request):
        value = Url.objects.filter(user = self.request.user)
        data = UrlShortnerSerializer(value,many = True)
        return Response(data)
    
    def create(self,request):
        serializer = UrlShortnerSerializer(data = request.data)
        if serializer.is_valid:
            generate_url = generate_random_urlskey()

            url = Url.objects.create(
                url = request.data.get('url'),
                user = request.user,
                urlCount = 0,
                shortend_url = generate_url
            )
            data = UrlShortnerSerializer(url).data

            return Response(data , status = status.HTTP_201_CREATED)
    
    def update(self,request,pk = None):
        value = self.get_object(pk)
        url = UrlShortnerSerializer(value,data=request.data)
        return Response(url.data)
    
    def destroy(self,request,pk =None):
        url = self.get_object(pk)
        url.delete()
        return Response(status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk =None):
        updatecount = Url.objects.filter(shortend_url = pk).update(urlCount = F('urlCount')+1)

        value = self.get_object(pk)

        serializer = UrlShortnerSerializer(value)
        return Response(serializer.data,status=status.HTTP_200_OK) 




