from django.db import models
from Article.models import Aticle,Comment
from django_mysql.models import JSONField
# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)#
    user_img = models.ImageField(upload_to='',height_field='',width_field='',max_length=100)
    user_pwd = models.CharField(max_length=2000)#加密后存储
    join_time = models.DateTimeField(auto_now=True)#加入时间
    user_email = models.EmailField()#
    user_phone = models.CharField(max_length=20,null=True)#用户电话
    user_addr = models.CharField(max_length=100,null=True)#居住地
    user_work = models.CharField(max_length=100,null=True)#职业
    user_hobby = models.CharField(max_length=300,null=True)#爱好
    user_url = models.URLField(null=True)#用户主页
    user_gitHub = models.URLField(null=True)#github地址
    user_attrs = JSONField()#用户其他信息
    article = models.ForeignKey(Aticle,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    class Meta:
        db_table = 'User_info'
        app_label = 'User'