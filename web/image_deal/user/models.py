from django.db import models

# Create your models here.
class user(models.Model):
	account = models.CharField('用户名',max_length=16)
	password = models.CharField('密码',max_length=20)
	login_time = models.DateTimeField('登录时间',auto_now_add=True)
	nickname = models.CharField('昵称',max_length=15)
	admin = models.CharField('身份',max_length=10)
	sex = models.BooleanField()
