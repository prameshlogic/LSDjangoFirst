from django.shortcuts import render
from .models import userModel
from rest_framework import viewsets
from .serializers import userSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = userModel.objects.all()
    serializer_class = userSerializer



# Create your views here.



