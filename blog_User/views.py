from django.shortcuts import render,redirect
from django.http import  HttpResponse,HttpResponseNotFound
# Create your views here.

def index(request):
    return render(request,'login.html')
    # return  HttpResponse('用户首页')

def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return  HttpResponse("用户注册")

def get_pwd(requests):
    """
    找回密码
    :param requests:
    :return:
    """
    return HttpResponse("找回密码")
