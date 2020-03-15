from django.urls import path,re_path
from . import views
app_name = 'blog_User'
urlpatterns =[
    # path('',views.index),
    path('login/',views.index),
    path('register/',views.register),
    path('forgetpwd/',views.get_pwd),
]