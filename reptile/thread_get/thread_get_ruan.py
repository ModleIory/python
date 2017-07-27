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
		#由于网络不好有时候这里会报个错
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
		# [(link,type),(link,type)]
		return match_arr

	def get_next_data(self):
		arr = self.get_main_data()
		rule_origin = r'<a\shref="(http://www.ruanyifeng.com/blog/\d{4}/\d{2}/.+?\.html)">(.+?)</a>'
		rule = re.compile(rule_origin)
		'''
		html = self.get_html(arr[0][0])
		print(html)
		rule = re.compile(rule_origin)
		print(re.findall(rule,html))
		'''
		save_arr = []
		for j in arr:
			#get essay title page
			html = self.get_html(j[0])
			title_arr = re.findall(rule,html)
			save_arr.append({'type':j[1],'title':title_arr})
		# print(save_arr)
		#[{type:essay_type,title:[(link,title)]}]
		return save_arr

	def get_last_data(self):
		arr = self.get_next_data()

		rule_origin = r'<p>(.+?)</p>'
		rule = re.compile(rule_origin)
		for j in arr:
			directory = j['type']
			for i in j['title']:
				title = i[1]
				link = i[0]
				cur_page = self.get_html(link)
				content_arr = re.findall(rule,cur_page)
				content = '\n\t'.join(content_arr)
				# print(content)
				q.put({"directory":directory,'title':title,'link':link,'content':content},block=True)
				print('得到一篇文章了!!!')



	def run(self):
		try:
			self.get_last_data()
		except Exception as e :
			with open('Mr.Ruan/error_log.log','a+',encoding='utf-8') as f:
				f.write(str(e)+'\n')



class save_data(threading.Thread):
	def __init__(self,q):
		super().__init__()
		print('Consumer begin to consume......')
		self.q = q
	def run(self):
		print('正在等待文章的出来')
		content = q.get(block=True)
		print(content)



create = get_data(q)
consumer = save_data(q)
create.start()
consumer.start()
create.join()
consumer.join()

print('All is ok ... ...')



