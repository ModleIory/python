#!/usr/bin/python3

#相当于controller，

from django.http import HttpResponse
from TestModel.models import Test


def save_data(req):
		print('*'*30)
		print(req.GET)
		instance = Test(name='aaamodldde',age=23,email='32322aaa2232@qq.com',time="2017-01-12")
		instance.save()
		return HttpResponse("数据添加成功！")

def get_data(req):
	list = Test.objects.all()
	print('*'*30)
	# so  list is like [{},{}]
	for x in list:
		print(x.name)
	each = Test.objects.get(id=1)
	print(each)
	return HttpResponse('得到了')

def update_data(req):
	# instance = Test.objects.get(id=1)
	# instance.name = 'fairy'
	# instance.save()
	Test.objects.filter(id=1).update(name='modle_sherlock')
	return HttpResponse('修改成功')

def delete_data(req):
	Test.objects.filter(id=5).delete()
	return HttpResponse('删除成功！')