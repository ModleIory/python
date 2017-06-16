#! -*- coding:utf-8 -*-
import re
import urllib.request
import urllib 

print('this is python reptile')

#url = http://www.yiibai.com/python/python3-webbug-series1.html
#研究字符串编码和二进制问题
def getHtml(url):
	page = urllib.request.urlopen(url)
	# print(type(page.read()))#是二进制的
	# gbk是中国久远的编码,不有英文,仅仅有些特殊的字符,很少,所以,不认识有的二进制编码,ignore就是不认识的管他娘,虽说不报错,但是乱码得很
	# html = page.read().decode('gbk','ignore')==> gbk utf-8 ascii
	html = page.read().decode('gbk')
	print(html)
	return html

def analyse(string):
	# rule = r"class=\"pubu_img_xiangao\slzload\"\s+src=\"(http://[a-zA-Z0-9/._]+\.jpg)\""
	rule = r"<img.+style=\"display:inline\">?"
	c_r = re.compile(rule)
	print(c_r)
	list_re = re.findall(c_r,string)
	print(list_re)

analyse(getHtml('http://sucai.redocn.com/tupian/renwutupian/'))
# string = ''' height="306" width="204" class="pubu_img_xiangao lzload" src="h
# ttp://img3.redocn.com/tupian/20150930/gongyu
# annvhaixiezhen_5021824_small.jpg"'''
# url = r"class=\"pubu_img_xiangao\slzload\"\s+src=\"(http://[a-zA-Z0-9/._]+\.jpg)\""
# c_r = re.compile(url)
# end = re.findall(c_r,string)
# print(end)



