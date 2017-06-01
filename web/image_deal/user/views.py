from django.shortcuts import render
from django.http import HttpResponse
from user.models import user
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
	u = json.loads(user_msg)
	account_exist = user.objects.filter(account=u['username'])
	if account_exist:
		return HttpResponse(json.dumps({'code':'-1','msg':'用户名存在！'}))
	try:
		instance = user(account=u['username'],password=u['password'],admin='normal',sex=1,nickname=u['username'])
		result = instance.save()
	except Exception as e:
		print('在保存用户时候发生异常'+e)
	else:
		end = {'code':0,'msg':'保存成功！'}
		return HttpResponse(json.dumps(end))

def do_login(req):
	account = req.GET['account']
	password = req.GET['password']
	result = user.objects.get(account=account,password=password)
	print(result)
	# print(result.account)
	# print(result.sex)
	# print(result.admin)
	if not result:
		return HttpResponse(json.dumps({'code':'1','msg':'用户名或者密码错误！'}))
	else:
		req.session['user'] = {'account':result.account,'sex':result.sex,'admin':result.admin}
		return HttpResponse(json.dumps({'code':'0','msg':'验证成功！'}))
		
