from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article,Comment
from tinymce.models import HTMLField
from django.db import models
from blog_User import user_decorator
# Create your views here.
#首页
@user_decorator.login
def index(request):
    Artics = Article.objects.all().order_by('-Fabulous_count')#点赞量倒叙排名
    context = {}
    context['articles']=Artics
    return  render(request,'Article/index.html',context)


#新随笔
@user_decorator.login
def newArticle(request):
    return render(request,'Article/new_article.html')



#文章详细界面
@user_decorator.login
def detailArticle(request,Article_Id):
    return HttpResponse(Article_Id)