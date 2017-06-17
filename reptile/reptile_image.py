#! -*- coding:utf-8 -*-
import re
import urllib.request
import urllib 
import os

print('this is python reptile , to download image from  a web')

#url = http://www.yiibai.com/python/python3-webbug-series1.html
#研究字符串编码和二进制问题
def getHtml(url):
	page = urllib.request.urlopen(url)
	# print(type(page.read()))#是二进制的
	# gbk是中国久远的编码,不有英文,仅仅有些特殊的字符,很少,所以,不认识有的二进制编码,ignore就是不认识的管他娘,虽说不报错,但是乱码得很
	# html = page.read().decode('gbk','ignore')==> gbk utf-8 ascii
	html = page.read().decode('gbk')
	# print(html)
	return html
#@string is all html code
#@rule is regular express 
def analyse(string,rule):
	compile_rule = re.compile(rule)
	#这里直接显示括号里面的推入数组
	list_re = re.findall(compile_rule,string)
	return list_re

def mkdir(path):
	path = path.strip()
	if not os.path.exists(path):
		os.makedirs(path,777)
	return path

def save_file(buf,path,name):
	new_path = mkdir(path)
	uri = "{}/{}".format(new_path,name)
	with open(uri,'wb') as file:
		file.write(buf)
		print('文件保存成功!文件名{}'.format(name))

def save_image(arr):
	count = 0
	for x in arr:
		buf = urllib.request.urlopen(x)
		binary_code = buf.read()
		# print(binary_code)
		# print(type(binary_code))
		save_file(binary_code,'download','{}.jpg'.format(count))
		count += 1

html_code = getHtml('http://sucai.redocn.com/tupian/renwutupian/')
rule = r"class=\"pubu_img_xiangao?\"\s+src=\"(http://[a-zA-Z0-9/._]+?\.jpg)\""
url_list = analyse(html_code,rule)
save_image(url_list)



