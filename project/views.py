from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
def homepage(request):
    return render(request,'project/index.html')
    

def profilepage(request):
    if request.user.is_authenticated:
        if request.user.typeof=='teacher':
            return render(request,'project/profilePage.html')
        else:
            return render(request,'project/profilePage2.html')

    else:
        return redirect('login')

def register(request):
    if(request.method=='GET'):
        return render(request, 'project/register.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                 user=User.objects.create_user(request.POST['username'],password=request.POST['password1'],typeof=request.POST['typeof'],imagpro=request.POST['imagpro'],datils=request.POST['datils'],where=request.POST['where'])
                 user.save()
                 login(request,user)
                 return redirect('profilepage')
            except IntegrityError:
                return render(request,'project/register.html',{'errormsg':'user exsist'})


        else:
           return render(request,'project/register.html',{'errormsg':'password dint match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home') 

def loginuser(request):
    if (request.method == 'GET'):
        return render(request, 'project/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'project/login.html', { "errMsg": "User doesn't exist" })
        else:
            login(request, user)
            return redirect('profilepage')
