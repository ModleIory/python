from django.db import models

# Create your models here.

class image(models.Model):
	statement = models.CharField('图片描述',max_length=50)
	url = models.CharField('储存路径',max_length=300)
	uid = models.IntegerField('用户id')
	time = models.DateTimeField('修改的时间',auto_now_add=True)
