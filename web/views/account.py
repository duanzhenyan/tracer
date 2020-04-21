"""
用户账号相关：注册、登录、重置密码
"""
from django.shortcuts import render


def register(requset):
    return render(requset, 'web/../templates/register.html')
