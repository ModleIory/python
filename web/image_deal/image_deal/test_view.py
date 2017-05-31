#!/usr/bin/python3

from django.http import HttpResponse
from django.shortcuts import render 

def test(req):
	return HttpResponse('测试成功！')