from django.db import models
from datetime import datetime

# Create your models here.
class Aticle(models.Model):
    article_id = models.CharField(max_length = 200 )
    tag = models.CharField(max_length = 200 )
    create_time = models.DecimalField(default = datetime.now())
    update_time = models.DecimalField(default = datetime.now())
    read_count = models.CharField(max_length = 200 )
    Fabulous_count = models.CharField(max_length = 200 )
    not_Fabulous = models.CharField(max_length = 200 )
    comment_count = models.CharField(max_length = 200 )
    comment_Fabulous = models.CharField(max_length = 200 )
    comment_not_Fabulous = models.CharField(max_length = 200 )
    article_type = models.CharField(max_length = 200 )
    article_url = models.CharField(max_length = 200 )
    attrs   = models.TextField

