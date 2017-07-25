#!/usr/bin/python3
#-*- coding:utf-8 -*-


#http://so.gushiwen.org/authors/的古诗的内容

import re
import sys , time ,os
import threading
import urllib.request

print('Begin to get by author')

class get_author(threading.Thread):
	def __init__(self):
		super().__init__()
		self._type = 'ancient_poem'

	def get_html(self,url):
		page = urllib.request.urlopen(url)
		return page.read().decode('utf-8')

	def get_main_page_data(self):
		url = 'http://so.gushiwen.org/authors'
		html = self.get_html(url)
		rule = r'<a\shref="/author_(\d+?).aspx">(.+?)</a>'	
		r = re.compile(rule)
		arr = re.findall(r,html)
		print(arr)
		return arr

	def get_second_page_data(self):
		#放下所有的[{title:content}...]
		all_dict = {}
		arr = self.get_main_page_data()

		#单个的解决
		#http://so.gushiwen.org/authors/authorsw_665A1.aspx
		# html = self.get_html('http://so.gushiwen.org/authors/authorsw_{}A1.aspx'.format(arr[0][0]))
		# print(html)
		# title_get
		# re_author = r'<b>(.+?)</b>'
		# rule_author = re.compile(re_author)
		# arr = re.findall(rule_author,html)
		# arr.pop()
		# arr.pop(0)
		# print(arr)
		# content_get
		# 这个确实很好用fuck  re.sub(new_parttern,old,string)
		# pure_html = re.sub(r'<br />|\n|<p>|</p>',' ',html)
		# re_content = r'<div\sclass="contson"\sid="contson.+?">(.+?)</div>'
		# # rule_content = re.compile(re_content)
		# # 有\n符号的还是要多行匹配,不要编译了 ,因为写\n根本写不完,麻烦
		# arr = re.findall(re_content,pure_html,re.M|re.S)
		# print(arr)
		# print(len(arr))

		title_re = r"<b>(.+?)</b>"
		title_rule = re.compile(title_re)
		#这里不编译了,因为要多行,编译了不可匹配re.M|re.S,来应对\n
		content_re = r'<div\sclass="contson"\sid="contson.+?">(.+?)</div>'
		#整体的解决 arr[(link_id,author)]
		for x in arr:
			tmp = []
			link = 'http://so.gushiwen.org/authors/authorsw_{}A1.aspx'.format(x[0])
			html = self.get_html(link)
			#出去多余的标签
			pure_html = re.sub(r'<br />|<p>|</p>','',html)
			title_arr = re.findall(title_rule,pure_html)
			#有两个多匹配的,首位各一个,去了
			title_arr.pop()
			title_arr.pop(0)
			content_arr = re.findall(content_re,pure_html,re.M|re.S)

			for k in range(len(title_arr)):
				tmp.append((title_arr[k],content_arr[k]))

			all_dict[x[1]] = tmp

		print(all_dict)
		# print(len(all_dict))
		return all_dict
			

	def save_poem(self,author,title,content):
		root_directory = self._type
		all_directory = root_directory+'/'+author
		document_path = all_directory+'/'+title+'.txt'
		try:
			if not os.path.exists(all_directory):
				os.makedirs(all_directory)
			with open(document_path,'w+',encoding='utf-8') as f:
				f.write(content)
		except Exception as e:
			print('出现了一个错误!')
			with open(root_directory+'/error_log.log','a+',encoding='utf-8') as error_log:
				error_log.write(str(e)+'\n')


	def run(self):
		data = self.get_second_page_data()
		#data{author:[{title:content}]}
		for x,y in data.items():
			for j in y:
				self.save_poem(author=x,title=j[0],content=j[1])



start = time.time()
test = get_author()
test.start()
test.join()
end = time.time()
print('总共花费时间是{}'.format(end-start))





