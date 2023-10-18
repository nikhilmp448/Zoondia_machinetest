from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import qrcode
import qrcode.image.svg
from io import BytesIO


# Create your views here.
class QRiewset(viewsets.ViewSet):
    def create(self,request):
        context = {}
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
        return Response(context,status=status.HTTP_200_OK)