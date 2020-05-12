from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.http import  HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from Article.models import  Article
from .models import *
import traceback
import json
# Create your views here.

def index(request,users=None):
    user_name = users
    # try:
    #     user_name = request.session['user_name']
    #     print("user_name:{}".format(user_name))
    # except:
    #     print("用户没有登录")
    #     return render(request, 'User/login.html')
    if user_name:
        user = get_object_or_404(User_info, user_name=user_name)
        context = {}
        context['users'] = user_name
        user_article = Article.objects.filter(user=user)
        print("该用户下的文章数量:%s"%user_article.count())
        paginator = Paginator(user_article,2)#分页 每页10篇
        # paginator = Paginator(Artics, 10)  # 分页 每页10篇
        page = request.GET.get('page')  # 获取url中的页码
        try:
            article_list = paginator.get_page(page)  # 获取对应页码返回
            context['articles'] = article_list

        except:
            traceback.print_exc()
        return render(request,'User/user-center.html',context)
    print("用户没有登录")
    return render(request,'User/login.html')

def deal_login(request):
    if request.method == "POST":
        ret = {"status": 0, 'url': '','info':''}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user_exit = User_info.objects.filter(user_name=user)
        if user_exit:
            if pwd == user_exit[0].user_pwd:#密码正确
                red = HttpResponseRedirect('/')
                ret['info'] = '登录信息核验通过'
                ret['url'] = '/'
                ret['status'] = 1
                red.set_cookie('user_name',user)
                request.session['user_id'] = user_exit[0].user_id
                request.session['user_name'] = user
                return HttpResponse(json.dumps(ret))
        else:
            ret['info'] = '用户名或密码不正确'
            ret['url '] = '/user/login/'
            ret['status'] = 2
            return HttpResponse(json.dumps(ret))
    return render(request, 'User/login.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    return render(request,'User/register.html')

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
        # print(userName, pwd, a_pwd, mail, tel, addr)
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
