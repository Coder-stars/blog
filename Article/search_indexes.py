from .models import Article
from haystack import  indexes


class ArticleIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    #对标题，标签，正文进行搜索
    title= indexes.CharField(model_attr='article_title')
    tags = indexes.CharField(model_attr='article_tag')
    content = indexes.CharField(model_attr='article_content')


    def get_model(self):
        return  Article


    def index_queryset(self, using=None):
        return self.get_model().objects.all()
    #每个索引里面必须有且只能有一个字段document=True