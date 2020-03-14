from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article,Comment

# Create your views here.
#首页
def index(request):
    Artics = Article.objects.all().order_by('-Fabulous_count')#点赞量倒叙排名
    context = {}
    context['articles']=Artics
    return  render(request,'Article/index.html',context)


#新随笔
def newArticle(request):
    return HttpResponse("写文章界面")



#文章详细界面
def detailArticle(request,Article_Id):
    return HttpResponse(Article_Id)