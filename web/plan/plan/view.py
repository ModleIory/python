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
	return render(req,'hello.html',context)