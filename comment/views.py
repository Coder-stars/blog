from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from Article.models import Article
from .forms import CommentForm
from blog_User.models import User_info
from blog_User import user_dectorator
from Article.views import detailArticle
from comment.models import Comment
# 文章评论
@user_dectorator.login
def post_comment(request,id,parent_comment_id=None):
    article = get_object_or_404(Article, article_id=id)
    user_name1 = request.session['user_name']
    user = get_object_or_404(User_info, user_name=user_name1)
    # 处理 POST 请求
    print("收到评论请求")
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = user
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')
            if not parent_comment_id:
                new_comment.save()
            # return detailArticle(request,article.article_id)
            return redirect('/Article/a-id/{}/'.format(article.article_id))
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': article.article_id,
            'parent_comment_id': parent_comment_id
        }
        return render(request, 'comment/reply.html', context)
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")