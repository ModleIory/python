from django.shortcuts import render
from django.http import HttpResponse
from user import models

# Create your views here.

def login(req):
	data = {}
	return render(req,'user/login.html',data)
