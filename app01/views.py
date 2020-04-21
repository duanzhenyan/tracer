from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
from django import forms
from django.core.validators import RegexValidator

from app01 import models
from django.conf import settings
import random


# Create your views here.
def send_sms(request):
    """
    发送短信
    :param request:
    ?tpl=login
    ?tpl=register
    :return:
    """
    tpl = request.GET.get("tpl")
    phone = request.GET.get("phone")

    tpl_id = settings.TENCENT_SMS_TEMPLATE[tpl]
    if not tpl_id:
        return HttpResponse("模板不存在")
    if not phone:
        return HttpResponse("手机号不能为空")
    code = random.randrange(1000, 9999)
    res = send_sms_single(phone, tpl_id, [code, ])
    if res['result'] == 0:
        return HttpResponse("成功")
    else:
        return HttpResponse(res['errmsg'])


class RegisterModelFrom(forms.ModelForm):
    mobile_phone = forms.CharField(label='手机号',
                                   validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', "手机号格式错误"), ])
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    code = forms.CharField(label='验证码', widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label, )


def register(request):
    form = RegisterModelFrom()
    return render(request, "app01/register.html", {"form": form})
