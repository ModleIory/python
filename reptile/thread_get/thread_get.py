#!/usr/bin/python3
#-*- coding:utf-8 -*-

#http://www.gushiwen.org的所有内容

import re
#这里必须这样写才行
import urllib.request
import os,sys 
import threading
import time

print('Use thread to get message from www.gushiwen.org and write into document')


#爬取古问
class get_guwen(threading.Thread):

	url = None
	re_main = None
	main_page_data = None
	re_second = None
	second_page_data = []
	re_third_title = None
	re_third_content = None
	type = 'ancient_book'

	def __init__(self,url,re_main='',re_second='',re_third_title='',re_third_content=''):
		print('\n'+'*'*50+'\n')
		print("Begin to get guwen")
		super().__init__()
		self.url = url
		#这里编译了 compile 那么我在用re.M|re.S修饰就会报错了真是奇怪
		self.re_main = re.compile(re_main)
		self.re_second = re.compile(re_second)
		self.re_third_title = re.compile(re_third_title)
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
					#详情title deal
					arr_title = re.findall(self.re_third_title,html)
					title = arr_title[0]
					print(title)
					#详情内容deal
					#表达式谢了\n这里就不用re.S|re.M
					content_with_html_arr = re.findall(self.re_third_content,html,re.M|re.S)
					content_with_html = content_with_html_arr[0]
					re_deal_html_content = r'<p>|</p>|\n'
					pure_content_arr = re.split(re_deal_html_content,content_with_html)
					content = '\n'.join(pure_content_arr)
					print(content)
					type = self.type
					book = x
					save_book(self.type,book,title,content)

	#保存书籍
	def save_book(type,book,title,content):
		directory = type+'/'+book
		path = directory+'/'+title+'.txt'
		try:
			if not os.path.exists(directory):
				os.makedirs(directory)
			#在window打开新文件的格式都是gbk的编码,所以要转化下
			with open(path,'w',encoding='utf-8') as file:
				all = title+'\n\n'+content
				result = file.write(all)
		except Exception as e:
			print('出现一个错误...')
			error_log = type+'/'+'error_log.log'
			with open(error_log,'a+',encoding='utf-8') as err:
				err.write(str(e)+'\n\n')


	def run(self): 
		self.get_third_page_data()	
		
#得到各本书籍url,名字的reg_exp
begin = time.time()
re_main = r'<a\shref="(/guwen/book_\d+?\.aspx)">(.+?)</a>'
re_second = r'<a\shref="(/guwen/bookv_\d+?\.aspx)">(.+?)</a>'
#有的地方title形式还不一样!
re_third_title = r'<h1.+?>\n(.+?)\n'
re_third_content = r'<div\sclass="contson">(.+?)</div>'
test = get_guwen('http://so.gushiwen.org/guwen/',re_main,re_second,re_third_title,re_third_content)
test.start()
test.join()
end = time.time()
print('time is : {}'.format(end-begin))

