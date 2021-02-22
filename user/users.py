from django.shortcuts import render, redirect
from login import models
from login.form import UserForm
from login.form import RegisterForm


def user(request):
    pass
    return render(request, "my-account.html")

