from django.shortcuts import render,redirect
from django.http import  HttpResponse,HttpResponseNotFound,HttpResponseRedirect

from .models import *
import traceback
import json
# Create your views here.

def index(request):
    return render(request,'login.html')

def deal_login(request):
    if request.method == "POST":
        ret = {"status": 0, 'url': '','info':''}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_exit = User_info.objects.filter(user_name=user)
        if user_exit:
            if pwd == user_exit[0].user_pwd:#密码正确
                # red = HttpResponseRedirect('/')
                ret['info'] = '登录信息核验通过'
                ret['url'] = '/'
                ret['status'] = 1
                # red.set_cookie('user_name',user)
                request.session['user_id'] = user_exit[0].user_id
                request.session['user_name'] = user
                return HttpResponse(json.dumps(ret))

        else:
            ret['info'] = '用户名或密码不正确'
            ret['url '] = '/user/login/'
            ret['status'] = 2

            return HttpResponse(json.dumps(ret))
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return render(request,'register.html')

def deal_register(request):
    if request.method == 'POST':
        userName = request.POST.get('user')
        pwd = request.POST.get('pwd')
        a_pwd = request.POST.get('a_pwd')
        mail = request.POST.get('emai')
        tel = request.POST.get('tel')
        addr = request.POST.get('addr')
        infos = {
            'user_name':userName,
            'user_pwd':pwd,
            'user_email':mail,
            'user_phone':tel,
            'user_addr':addr,
        }
        print(userName, pwd, a_pwd, mail, tel, addr)
        user = User_info.objects.filter(user_name=userName).exists()
        if pwd == a_pwd:
            if user:
                content = {
                    'info':'用户名已经存在，换个用户名试试呗',
                    'url':'/user/register/',
                    'status':2,}#用户名存在
            else:
                try:
                    User_info.objects.create(**infos)
                    content = {
                        'info':'注册成功，自动跳转登录界面.......',
                               'url':'/user/login/',
                               'status':1,#注册成功
                               }
                    return  HttpResponse(json.dumps(content))
                except:
                    traceback.print_exc()
                    return HttpResponse(traceback.format_exc())
            return HttpResponse(json.dumps(content))
        else:
            return HttpResponse('两次密码不一致')




def get_pwd(requests):
    """
    找回密码
    :param requests:
    :return:
    """
    return HttpResponse("找回密码")
