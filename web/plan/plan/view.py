#!/usr/bin/python3
#-*- coding:utf-8 -*-

#这个相当于控制器

from django.http import HttpResponse
from django.shortcuts import render

def hello(req):
	return HttpResponse("hello world!")


def show(req):
	context = {}
	context['hello'] = "this is template test"
	context['count'] = 10
	context['flag'] = True
	context['list'] = [
		{"name":"wuruijie","age":23,"saying":"king"},
		{"name":"zhongyaji","age":22,"saying":"yoyo"}
	]
	context['variable'] = 'Variable deep knew ok yes'
	return render(req,'hello.html',context)

def extends(req):
	context = {}
	context['title'] = '模板的继承'
	return render(req,'son.html',context)