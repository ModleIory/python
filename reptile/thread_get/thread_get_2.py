#!/usr/bin/python3
#-*- coding:utf-8 -*-


#http://so.gushiwen.org/authors/的古诗的内容

import re
import sys , time 
import threading
import urllib.request

print('Begin to get by author')

class get_author(threading.Thread):
	def __init__(self):
		super().__init__()

	def get_html(self,url):
		page = urllib.request.urlopen(url)
		return page.read().decode('utf-8')

	def get_main_page_data(self):
		url = 'http://so.gushiwen.org/authors'
		html = self.get_html(url)
		rule = r'<a\shref="/author_\d+?.aspx">(.+?)</a>'	
		r = re.compile(rule)
		arr = re.findall(r,html)
		# print(arr)
		return arr

	def run(self):
		self.get_main_page_data()
		# print(self.get_html('http://so.gushiwen.org/authors'))



start = time.time()
test = get_author()
test.start()
test.join()
end = time.time()
print('总共花费时间是{}'.format(end-start))





