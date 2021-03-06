# login/models.py

from django.db import models


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    full_name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    country = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')#性别选择，默认是男
    c_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
