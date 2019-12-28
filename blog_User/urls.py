from django.urls import path,re_path
from . import views
app_name = 'blog_User'
urlpatterns =[
    path('',views.index)
]