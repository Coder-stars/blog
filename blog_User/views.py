from django.shortcuts import render,redirect
from django.http import  HttpResponse,HttpResponseNotFound
# Create your views here.

def index(request):
    return render(request,'login.html')
    # return  HttpResponse('用户首页')