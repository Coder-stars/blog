from django.urls import path,re_path
from . import views
app_name = 'Article'
urlpatterns =[
    path('',views.index),#首页，文章列表
    path('new/',views.newArticle),#write article
    re_path('id=(\d+)/$',views.detailArticle),#article detaile
]