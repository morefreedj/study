from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):#form表单里的东西一定需与前端一致
    username = forms.CharField(label ="用户名", max_length=128)
    password = forms.CharField(label="密码",max_length=256, widget=forms.PasswordInput)
    captcha  = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
    password1 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput)
    email = forms.EmailField(label="邮箱地址")
    fullname = forms.CharField(label="真名全名")
    captcha = CaptchaField(label='验证码')
