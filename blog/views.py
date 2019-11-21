from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth



def home(request):
    title ='Home'
    return render(request,'index.html',{'title':title})

def about(request):
    title='about'
    return render(request,'about.html',{'title':title})
    

def logout(request):
    auth.logout(request)
    return redirect('/')