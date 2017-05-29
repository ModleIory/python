#!/usr/bin/python3
#-*- coding:utf-8 -*-

from django.http import HttpResponse

def hello(req):
	return HttpResponse("hello world!")