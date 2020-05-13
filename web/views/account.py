"""
用户账号相关：注册、登录、重置密码
"""
from django.shortcuts import render
from web.forms.account import RegisterModelFrom


def register(requset):
    form = RegisterModelFrom()
    return render(requset, 'register.html', {"form": form})
