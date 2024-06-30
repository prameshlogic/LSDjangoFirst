from django.shortcuts import render,redirect
from .models import userModel
from rest_framework import viewsets
from .serializers import userSerializer

# Create your views here.


class userViewSet(viewsets.ModelViewSet):
    queryset = userModel.objects.all()
    serializer_class = userSerializer


def hmpage(request):
    return render(request,"invest.html")

def lgpage(request):
    return render(request,"login.html")
    
def login(request):
    if request.method == 'POST':
            return render(request,"a.html")
        
        


