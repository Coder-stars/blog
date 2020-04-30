from django.db import models
from mptt.models import TreeForeignKey,MPTTModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from Article.models import Article
from blog_User.models import User_info
# Create your models here.

# 博文的评论
class Comment(MPTTModel):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User_info,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = RichTextField()
    # body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[:20]
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        User_info,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    # 替换 Meta 为 MPTTMeta
    # class Meta:
    #     ordering = ('created',)
    class MPTTMeta:
        order_insertion_by = ['created']

