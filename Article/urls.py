from django.urls import path,re_path
from . import views
app_name = 'Article'
urlpatterns =[
    path('',views.index),#首页，所有用户文章列表
    # path('page=<int:id>/'.views.index),
    re_path('^new/',views.newArticle),#新建文章
    path('a-id/<int:Id>/',views.detailArticle,name='a_id',),#文章详情界面
    re_path("^deal_article/$",views.deal_article),#处理文章入库并返回概要界面
    re_path("^zan_article/$",views.zan),#点赞文章
    re_path("^not_zan_article/$",views.zan),#倒彩文章
]