from django.urls import path,re_path
from . import views
app_name = 'blog_User'
urlpatterns =[
    # path('',views.index),
    path('login/',views.index),
    path('deal_login/',views.deal_login),
    path('register/',views.register),
    path('deal_register/',views.deal_register),
    path('forgetpwd/',views.get_pwd),
]