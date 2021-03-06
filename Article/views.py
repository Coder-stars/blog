from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.shortcuts import render, redirect
import json
from .models import Article
from blog_User.models import User_info
from tinymce.models import HTMLField
from django.core.paginator import Paginator
from comment.models import Comment
from blog_User import user_dectorator
import traceback
from comment.forms import CommentForm
# Create your views here.


#首页
def index(request):
    context = {}
    Artics = Article.objects.all().order_by('-Fabulous_count')#点赞量倒叙排名
    paginator = Paginator(Artics,2)#分页 每页10篇
    # paginator = Paginator(Artics,10)#分页 每页10篇
    page = request.GET.get('page')#获取url中的页码
    articles = paginator.get_page(page)#获取对应页码返回

    context['articles'] = articles
    return render(request,'Article/index.html',context)

from .forms import articleForm
#新随笔
@user_dectorator.login
def newArticle(request):
    context={}
    aForm = articleForm()
    context['articleForm'] = aForm
    return render(request,'Article/new_article.html',context)


@user_dectorator.login
def deal_article(request):
    """
    新建文章入库并展示概要
    :param request: 文章详情（需要入库的数据）
    :return: 文章入库并文章概要界面
    """
    if request.method == 'POST':
        article = dict()
        title = request.POST.get('title')
        article_form = articleForm(request.POST)
        new_form = article_form.save(commit=False)
        new_form.user_id = request.session['user_id']
        new_form.save()
        # print(new_form.article_content)
        text = new_form.article_content
        tags = request.POST.get('tags')
        type = request.POST.get('type')
        article['article_title'] = title
        article['article_content'] = text
        article['article_outline'] = ''#前台取的时候直接取正文然后过滤
        article['article_type'] = True if str(type).strip() == 'open' else False
        article['article_tag'] = tags
        try:
            user_id = request.session['user_id']
            # print("------"*3)
            # print(user_id)
            user = User_info.objects.filter(user_id=user_id)[0]
            article['user'] = user
            print("获取用户信息成功")
        except:
            traceback.print_exc()
            print("获取用户信息出错")
        try:
            print(article)
            at = Article.objects.create(**article)
            print("文章保存成功")
            #返回概览视图或者用户中心
            return detailArticle(request,at.article_id)
        except Exception:
            print("文章保存异常")
            traceback.print_exc()

    # return  HttpResponse("处理文章入库并展示概要界面")


#文章详细界面
def detailArticle(request,Id):
    context = {}
    article = Article.objects.filter(article_id=Id)[0]
    context['title'] = article.article_title
    context['tag'] = article.article_tag
    context['type'] = article.article_type
    context['cont'] = article.article_content
    context['created'] = article.create_time
    context['focus'] = article.Fabulous_count
    context['not_focus'] = article.not_Fabulous
    context['read_count'] = article.read_count
    context['user_info'] = article.user
    print("文章作者%s"%article.user)
    context['article_id'] = article.article_id
    #阅读量加一
    article.read_count = int(context['read_count']) +1
    article.save()
    # 取出文章评论
    comment_form = CommentForm()
    comments = Comment.objects.filter(article_id=article.article_id)
    context['comments'] = comments
    context['comment_count'] = comments.count()
    context['comment_form'] = comment_form
    print("该文章共有:{} 条评价".format(comments.count()))
    return render(request,'Article/detail_article.html',context)


#点赞文章
@user_dectorator.login
def zan(request):#点赞与倒彩函数
    """
    通过type区分点赞与倒彩，实现点赞与倒彩功能
    :param request:
    :return:
    """
    if request.method == 'POST':
        artic_id = request.POST.get('article_id')
        type = request.POST.get('type')
        if str(type).strip() == 'zan':#只有点赞能通过请求
            ret = dict()
            try:
                article = Article.objects.filter(article_id=artic_id)[0]
                article.Fabulous_count +=1#文章点赞量增加一
                article.save()
                print("点赞成功")
                ret['status'] =1#返回前台成功状态码
            except:
                print("error happen")
                traceback.print_exc()
            return HttpResponse(json.dumps(ret))
        if str(type).strip() == 'not_zan':#倒彩
            ret = dict()
            try:
                article = Article.objects.filter(article_id=artic_id)[0]
                article.not_Fabulous +=1#文章倒彩量增加一
                article.save()
                print("倒彩成功")
                ret['status'] =1#返回前台成功状态码
            except:
                print("error happen")
                traceback.print_exc()
            return HttpResponse(json.dumps(ret))


