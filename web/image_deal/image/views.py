from django.shortcuts import render
from django.http import HttpResponse
import json
from image.models import image

# Create your views here.

def show_image(req):
	data = {}
	data['title'] = '成功提示页面'
	userInfo = req.session.get('user')
	print(userInfo)
	print(type(userInfo))
	data['user'] = userInfo
	return render(req,'image/show_image.html',data)

