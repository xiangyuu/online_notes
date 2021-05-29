from django.shortcuts import render

# Create your views here.
from . import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def reg_view(request):
    if request.method=="GET":
        return render(request,'user/register.html')
    elif request.method=="POST":
        username=request.POST.get('username','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        if len(username)<6:
            username_error='用戶名太短！'
            return render(request,'user/register.html',locals())
        elif len(password1)==0:
            password1_error= '密碼不能為空！'
            return render(request,'user/register.html',locals())
        elif len(password2)==0:
            password2_error= '密碼不能為空！'
            return render(request,'user/register.html',locals())
        elif password1 != password2:
            password2_error='密碼不相同！'
            return render(request,'user/register.html',locals())
        try:
            auser=models.User.objects.get(username=username)
            username_error='用戶名已存在！'
            return render(request,'user/register.html',locals())
        except:
            auser = models.User.objects.create(username=username,
                                               password=password1)
            html='註冊成功,<a href="/user/login">點我返回登入頁面</a>'
            resp=HttpResponse(html)
            resp.set_cookie('username',username)
            return resp

def login_view(request):
    if request.method=="GET":
        username=request.COOKIES.get('username','')
        return render(request,'user/login.html',locals())
    elif request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='':
            username_error='用戶名不能為空！'
            return render(request,'user/login.html',locals())
        elif password=='':
            password_error='密碼不能為空！'
            return render(request,'user/login.html',locals())
        try:
            auser=models.User.objects.get(username=username,
                                    password=password)
            request.session['user']={
                'username':username,
                'id':auser.id
            }
            resp=HttpResponseRedirect('/')
            if 'remember' in request.POST:
                resp.set_cookie('username',username)
            return resp

        except:
            login_error='用戶名或密碼不正確'
            return render(request,'user/login.html',locals())

def logout_view(request):
    if 'user' in request.session:
        del request.session['user']
        return HttpResponseRedirect('/')