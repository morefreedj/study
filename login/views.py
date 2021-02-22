# login/views.py

from django.shortcuts import render, redirect
from . import models
from .form import UserForm
from .form import RegisterForm

def index(request):
    pass
    return render(request, 'index.html')


def login_register(request):
    #'login_form':login_form,
    #'register_form': register_form
    login_form = UserForm#将form表单传递，当前的主要目的是可以传captcha验证码,如果不加的话，在首次跳转的时候就不会显示出来验证码
    register_form = RegisterForm
    return render(request, 'login-register.html', {'login_form': login_form, 'register_form': register_form})

def login(request):#前端对应login-register.html第505行

    if request.session.get('is_login',None):
        return redirect('/index/')

    if request.method == "POST":
        login_form = UserForm(request.POST)

        if login_form.is_valid():

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = models.User.objects.get(user_name=username)

                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id']  = user.id
                    request.session['user_name']= user.user_name
                    refresh = request.getSession().getAttribute("refresh")
                    return redirect('/index/')

                else:
                    message = "密码有误"
            except:
                message = "用户名不存在"
    #login_form = UserForm   #如果加上会导致captcha的错误信息传不上去
    return render(request, 'login-register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index')
    request.session.flush()  #注销session
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/index/')


def register(request):
    if request.session.get('is_login',None):
        #已登录状态不允许注册，直接跳转至首页
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = register_form
        if register_form.is_valid():

            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            password1= register_form.cleaned_data['password1']
            email    = register_form.cleaned_data['email']
            fullname = register_form.cleaned_data['fullname']
            #检验两次输入密码是否一样的代码已在前端写过，此处不再判断
            if password == password1:
                same_username = models.User.objects.filter(user_name=username)
                if same_username:
                    message = "用户名已存在"
                    return render(request, 'login-register.html', locals())
                same_email = models.User.objects.filter(email=email)
                if same_email:
                    message = "该邮箱已经被注册，如果确认是你的个人邮箱请联系我"
                    return render(request, 'login-register.html', locals())

                else:
                    #没有问题就开始创建
                    new_user = models.User.objects.create()
                    new_user.user_name = username
                    new_user.password  = password1
                    new_user.email     = email
                    new_user.full_name = fullname
                    new_user.save()
                    return redirect('/index/')


    return render(request, 'login-register.html', locals())

def contact (request):
    pass
    return render(request, 'contact.html')

def about (request):
    pass
    return render(request, 'about.html')