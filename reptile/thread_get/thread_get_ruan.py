#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os,time,sys,queue ,re
import threading
import urllib.request

print('Get data from Mr.Ruan and with creator-Consumer model')

q = queue.Queue()

class get_data(threading.Thread):
	def __init__(self,q):
		super().__init__()
		print('Creator begin to create......')
		self.q = q
		self.entry = "http://www.ruanyifeng.com/blog/startup/"
	def get_html(self,url):
		document = urllib.request.urlopen(url)
		html = document.read().decode('utf-8')
		# print(html)
		return html
	def get_main_data(self):
		html = self.get_html(self.entry)
		rule_origin = r'<a\shref="(.+?)"\stitle=".+?">(.+?)</a>'
		rule = re.compile(rule_origin)
		match_arr = re.findall(rule,html)
		# print(match_arr)
		# [(link,title),(link,title)]
		return match_arr
	def get_next_data(self):
		arr = self.get_main_data()
		rule_origin = r'<a\shref="(http://www.ruanyifeng.com/blog/\d{4}/\d{2}/.+?\.html)">(.+?)</a>'
		html = self.get_html(arr[0][0])
		print(html)
		print(re.findall(rule_origin,html))
		'''
		for j in arr:
			print(j[1])
			html = self.get_html(j[0])
			# title_list = re.findall(rule_origin,html,re.M|re.S)
			# print(title_list)
			# print(j[0])
		'''
	def run(self):
		self.get_next_data()

class save_data(threading.Thread):
	def __init__(self,q):
		super().__init__()
		print('Consumer begin to consume......')
		self.q = q
	def run(self):
		pass

create = get_data(q)
# consumer = save_data(q)
create.start()
# consumer.start()
create.join()
# consumer.join()

print('All is ok ... ...')



