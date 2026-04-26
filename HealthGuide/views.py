from django.shortcuts import render
from .models import Diseases,Emergency

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def GetAllDiseases(req):
    diseases=Diseases.objects.all().order_by("-id")
    data=[]
    for Data in diseases:
        data.append({
            "id":Data.id,
            "title":Data.title,
            "Description":Data.Description,
            "image":req.build_absolute_uri(Data.image.url) if Data.image else None
        })
    
    return Response({"data":data})

@api_view(["GET"])
def GetAllEmergency(req):
    emergency=Emergency.objects.all().order_by("-id")
    data=[]
    for Data in emergency:
        data.append({
            "id":Data.id,
            "title":Data.title,
            "Description":Data.Description,
            "video":req.build_absolute_uri(Data.video.url) if Data.video else None
        })
    
    return Response({"data":data})