from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def find_one(req):
	instance = models.Test(name='fuck',age=20,time='2017-01-22',email='232323@qq.com')
	instance.save()
	return HttpResponse('搞好了')

