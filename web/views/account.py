"""
用户账号相关：注册、登录、重置密码
"""
from django.shortcuts import render
from web.forms.account import RegisterModelFrom, SendSmsForm
from django.shortcuts import render
from django.http import JsonResponse


def register(request):
    form = RegisterModelFrom()
    return render(request, 'register.html', {"form": form})


def send_sms(request):
    """
    发送短信
    :param request:
    ?tpl=login
    ?tpl=register
    :return:
    """
    sms_from = SendSmsForm(request, data=request.GET)
    if sms_from.is_vaild:
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': sms_from.errors})
