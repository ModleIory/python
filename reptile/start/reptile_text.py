import urllib
import urllib.request
import os
import re

print('this is reptile and collection all the name of image')
#http://sucai.redocn.com/tupian/renwutupian

def get_html(url):
	http_obj = urllib.request.urlopen(url)
	html_buf = http_obj.read()
	html = html_buf.decode('gbk')
	# print(html)
	return html

def analyse(html,rule):
	compile_rule = re.compile(rule)
	result_list = re.findall(compile_rule,html)
	print(result_list)
	return result_list

def mkdir(path):
	path = path.strip()
	if not os.path.exists(path):
		os.makedirs(path)
	return path

def save_file(buf,path,name):
	uri = "{}/{}".format(path,name)
	with open(uri,'ab') as file:
		file.write(buf)
	

def final_deal(arr,path,name):
	for x in arr:
		txt = x+'\n'
		binary = txt.encode('utf-8')
		save_file(binary,path,name)
		print('标题记录成功!')

	

#<a href="http://sucai.redocn.com/tupian/5381815.html" target="_blank" class="hd-link-color">滑滑板的人</a>

html = get_html('http://sucai.redocn.com/tupian/renwutupian/')
rule = r'class="hd-link-color">(.+?)</a>'
url_list = analyse(html,rule)
save_path = 'download'
name = 'file.log'
final_deal(url_list,save_path,name)