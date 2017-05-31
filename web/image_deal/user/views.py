from django.shortcuts import render
from django.http import HttpResponse
from user import models
import json

# Create your views here.

def login(req):
	data = {}
	data['title'] = '用户登录'
	return render(req,'user/login.html',data)

def register(req):
	data = {}
	data['title'] = '用户注册'
	return render(req,'user/register.html',data)

def save_user(req):
	user_msg = req.POST['msg']
	print(user_msg)
	user_dic = json.loads(user_msg)
	print(user_dic)
	return HttpResponse('ok')
