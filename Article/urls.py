from django.urls import path,re_path
from . import views
app_name = 'Article'
urlpatterns =[
    path('',views.index)
]