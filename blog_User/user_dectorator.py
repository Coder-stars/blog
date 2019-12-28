from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# 如果未登录则转到登录界面


def login(fun):
    def login_func(request, *args, **kwargs):
        if request.session.get('user_id'):
            return fun(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_func
