from pyexpat.errors import messages
from django.db import IntegrityError
from django.shortcuts import render,redirect
from .models import userModel,sgModel
from rest_framework import viewsets
from .serializers import userSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


class userViewSet(viewsets.ModelViewSet):
    queryset = userModel.objects.all()
    serializer_class = userSerializer


def hmpage(request):
    return render(request,"invest.html")

def lgpage(request):
    return render(request,"login.html")
    
    
def signpage(request):  #sign and signup page can be merged using if else
    return render(request,"signup.html")        

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        umail = request.POST.get('mail')
        pwd = request.POST.get('pwd')

        if not (uname and umail and pwd):
            return render(request, 'signup.html', {'allexists': True})

        try:
            a = sgModel.objects.create(
                uname=uname,
                pwd=pwd,  
                umail=umail,
            )
            a.set_password(pwd)
            a.save()
            return redirect('login') 

        except IntegrityError:
            return render(request, 'signup.html', {'username_exists': True})

    return render(request, 'signup.html', {})

def login(request): #login and lgpage can be merged using ifelse
    if request.method == 'POST':
        luname = request.POST.get('luname')
        lpwd = request.POST.get('lpwd')

        try:
            # Fetch the user from the sgModel
            user = sgModel.objects.get(uname=luname)
            if user.check_password(lpwd):
                print("Redirecting to Profile page")
                # Password is correct, log the user in
                return render(request, 'profileEdit.html',{'user':user})
            else:
                # Password is incorrect
                return render(request, 'login.html', {'password_incorrect': True})
        except sgModel.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'user_not_found': True})
    else:
        return render(request, 'login.html')


def profileCreate(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        umail = request.POST.get('umail')
        pwd = request.POST.get('pwd')

        try:
            user = sgModel.objects.create(uname=uname, umail=umail, pwd=pwd) 
            user.save()
            return redirect('profileEdit', pk=user.pk)
        except IntegrityError:
            return render(request, 'profileEdit.html')

    return render(request, 'profileEdit.html')


def profileDelete(request, pk):
    user = get_object_or_404(sgModel, pk=pk)

    if request.method == 'POST':
        
        
        return redirect('hmpage')

    return render(request, "invest.html", {'user': user})


def profileEdit(request, pk):
    user = get_object_or_404(sgModel, pk=pk)

    if request.method == 'POST':
        uname = request.POST.get('uname')
        umail = request.POST.get('umail')
        pwd = request.POST.get('pwd')

        if not (uname and umail and pwd):
            messages.error(request, "All fields are required.")
            return render(request, 'profileEdit.html', {'user': user})

        user.uname = uname
        user.umail = umail
        user.pwd = pwd
        user.save()
        return redirect('profileEdit', pk=user.pk)

    return render(request, "profileEdit.html", {'user': user})


