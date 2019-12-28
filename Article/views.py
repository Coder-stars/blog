from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article,Comment

# Create your views here.
def index(request):
    Artics = Article.objects.all()
    context = {}
    context['articles']=Artics
    return  render(request,'Article/index.html',context)