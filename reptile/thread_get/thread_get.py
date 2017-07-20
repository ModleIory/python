#!/usr/bin/python3

#http://www.gushiwen.org的所有内容

import re
#这里必须这样写才行
import urllib.request
import os,sys 
import threading
import time

print('Use thread to get message from www.gushiwen.org and write into document')


class get_guwen(threading.Thread):

	url = None
	re_main = None
	main_page_data = None
	re_second = None
	second_page_data = []
	re_third_title = None
	re_third_content = None

	def __init__(self,url,re_main='',re_second='',re_third_title='',re_third_content=''):
		print('\n'+'*'*50+'\n')
		print("Begin to get guwen")
		super().__init__()
		self.url = url
		self.re_main = re.compile(re_main)
		self.re_second = re.compile(re_second)
		self.re_third_title = re_third_title
		self.re_third_content = re_third_content

	def get_html(self,url):
		document = urllib.request.urlopen(url)
		html = document.read().decode('utf-8')
		return html

	#得到首页的数据
	def get_main_page_data(self):
		#得到所有古籍
		html = self.get_html(self.url)
		arr = re.findall(self.re_main,html)
		return arr

	#得到二级页面数据<a href="/guwen/bookv_21.aspx">八佾篇</a>
	def get_second_page_data(self):
		father = self.get_main_page_data()
		all = []
		#输出每古籍的所有篇章
		for x in father:
			# print(x[0])
			html = self.get_html('http://so.gushiwen.org{}'.format(x[0]))
			arr = re.findall(self.re_second,html)
			all.append({x[1]:arr})
		# print(all)
		return all

	#得到三级的,就是题目和正文
	def get_third_page_data(self):
		grade_father = self.get_second_page_data()#[ {book_name:[(link,directory),(link,directory)]} ]
		count = 1
		for j in grade_father:
			#j is dictionary
			for x,y in j.items():
				#x is book_name , y is list os directory
				for k in y:
					html = self.get_html('http://so.gushiwen.org{}'.format(k[0]))
					arr_title = re.findall(self.re_third_title,html,re.M|re.S)
					print(html)
					# print(arr_title)
					if count==1:
						sys.exit()
			########### fuck metion there  because of  reg_exp can't get the title JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ


	def run(self):
		self.get_third_page_data()	
		
#得到各本书籍url,名字的reg_exp
begin = time.time()
re_main = r'<a\shref="(/guwen/book_\d+?\.aspx)">(.+?)</a>'
re_second = r'<a\shref="(/guwen/bookv_\d+?\.aspx)">(.+?)</a>'
re_third_title = r'<h1.+?>\n(.+?)\n<a'
test = get_guwen('http://so.gushiwen.org/guwen/',re_main,re_second)
test.start()
test.join()
end = time.time()
print('time is : {}'.format(end-begin))

