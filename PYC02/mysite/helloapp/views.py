from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from helloapp import models

user_list = []

def hello(request):
    #return HttpResponse("Hello World! I am coming...")

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     print(username,password)
    #     temp = {'user': username, 'pwd': password}
    #     user_list.append(temp)
    # return render(request, 'index.html', {'data': user_list})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 将数据保存到数据库
        models.UserInfo.objects.create(user = username, pwd = password)

    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})