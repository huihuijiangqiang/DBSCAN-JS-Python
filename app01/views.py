from django.shortcuts import render, HttpResponse, redirect
from sklearn.datasets import make_moons
from app01 import dataset
import json
import numpy
# Create your views here.
def index(request):
    """
    
    :param request: 请求相关的所有数据对象
    :return: 
    """
    # return HttpResponse("你好")

    if request.method == "POST":
        print(request)
        print(request.POST)
        print(type(dataset.X))
        return HttpResponse(json.dumps(dataset.X.tolist()))

    return render(request, "index.html")

    # return redirect("https://www.mzitu.com")


def ajax(request):
    print(request.is_ajax())  # 是否是ajax请求
    if request.method == 'GET':  # 获取get请求数据
        number = request.GET.get('number', None)
        noise = request.GET.get('noise', None)
    if request.method == 'POST':  # 获取post请求数据
        number = request.POST.get('number', None)
        noise = request.POST.get('noise', None)
    print(number,noise)
    print(type(float(noise)))
    X, y = make_moons(n_samples=int(number), noise=float(noise))
    # 1、 返回字符串类型数据
    # return HttpResponse('OK')  # ***
    # print(request.POST)
    # 2、 返回json类型数据
    print(X)
    data = json.dumps(json.dumps(X.tolist()), ensure_ascii=False)
    # data = json.dumps(json.dumps(dataset.X.tolist()), ensure_ascii=False)
    # 直接返回json模块处理后的json数据(json字符串)，前台接收到的是一个json类型的字符串，需要前台自己处理
    # return HttpResponse(data)
    # 返回json字符串是，还告诉前台，该数据就是json类型字符串，设置响应头
    return HttpResponse(data, content_type='application/json')  # ****

    # from django.http import JsonResponse
    # 3、返回json类型数据的终极方法
    # dic = {'status': 'ok', 'msg': '登录成功'}
    # return JsonResponse(dic, safe=False, json_dumps_params={'ensure_ascii': False})  # *****
    # 参数含义：
    # 返回值保证是字典类型
    # safe在False情况下就支持返回列表或字符串
    # 取消json的dumps方法采用的默认ascii编码中文