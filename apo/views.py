from django.shortcuts import render


# Create your views here.


def index(request):
    '''
    访问首页
    :param request: 发送请求
    :return:
    '''
    return render(request, 'login-page.html')
