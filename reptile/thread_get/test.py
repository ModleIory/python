import re
import urllib.request

# page = urllib.request.urlopen('http://so.gushiwen.org/guwen/bookv_19.aspx')
# html = page.read().decode('utf-8')
# print(html)

# rule = r'<h1.+?>\n(.+?)\n'
# arr = re.findall(rule,html,re.M|re.S)
# print(arr)

# rule_c = r'<div\sclass="contson">(.+?)</div>'
# arr_c = re.findall(rule_c,html,re.M|re.S)
# print(arr_c)

# print('*'*40)
# new_html  = arr_c[0]
# arr_c_deal = r'<p>|</p>|\n'
# out_html = re.split(arr_c_deal,new_html)
# print(out_html)
# print('\n'.join(out_html))

# import os 
# type = 'ancient_book'
# book = '左转'
# title = '告子上'
# content = "念如执盾,攻而不破"

# def save_book(type,book,title,content):
# 	directory = type+'/'+book
# 	path = directory+'/'+title+'.txt'
# 	if not os.path.exists(directory):
# 		os.makedirs(directory)
# 	with open(path,'w') as file:
# 		all = title+'\n\n'+content
# 		result = file.write(all)

# save_book(type,book,title,content)

# try:
# 	fuck
# except Exception as e:
# 	print(e)
# 	print(str(e))

va = {'nihao':'wangyuanzhong'}
print(list(va.keys()))
print(va.values())
print(list(va))