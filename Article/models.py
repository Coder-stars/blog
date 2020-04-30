from django.db import models
from tinymce.models import HTMLField
from  ckeditor.fields import RichTextField
from django.urls import reverse
from blog_User.models import User_info
from datetime import datetime
from django.utils import timezone

# from django_mysql.models import JSONField#    bug required mysql5.7+
# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=200)  # 文章标题
    article_outline = models.CharField(max_length=2000)#文章概要
    # article_content = HTMLField()  # 文章正文
    article_content = RichTextField()  # 文章正文
    article_tag = models.CharField(max_length = 200 ) #python  django 文章类别
    create_time = models.DateTimeField(default=timezone.now())#创建时间
    update_time = models.DateTimeField(auto_now=True)#更新时间
    read_count = models.IntegerField(default=0 )#阅读量
    Fabulous_count = models.IntegerField(default=0)#点赞量
    not_Fabulous = models.IntegerField(default=0)#倒彩量
    article_type = models.BooleanField(default=True )#文章类型 私有公开 默认公开
    article_url = models.CharField(max_length = 200,null=True,blank=True)#文章分享链接
    # attrs   = JSONField()#其他信息
    user = models.ForeignKey('blog_User.User_info',on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title

        # 获取文章地址
    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])
    class Meta:
        ordering = ('-create_time',)#默认返回最新文章
        db_table = 'Article_list'
        app_label = 'Article'






