from django.shortcuts import render,HttpResponse


# Create your views here.


def index(request):
    '''
    访问首页
    :param request: 发送请求
    :return:
    '''
    return render(request, 'login-page.html')

def detail(request):
    '''
    访问详情页
    :param request:
    :return:
    '''
    return HttpResponse('访问到了information！！！')

def safe(request):
    '''
    安全功能
    :param request:
    :return:
    '''
    return HttpResponse('wc方向，安全！')

