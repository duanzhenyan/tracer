from django.shortcuts import render, HttpResponse
from utils.tencent.sms import send_sms_single
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