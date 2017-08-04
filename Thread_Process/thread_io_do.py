import threading
import os 
import time
import urllib.request

print('同步和异步读取内容对比')

start = time.time()

#'''同步的处理
page = urllib.request.urlopen('https://cdn.bootcss.com/vue/2.4.2/vue.js')
print(page)	
document = page.read().decode('utf-8')
# print(document)

page_ = urllib.request.urlopen('https://cdn.bootcss.com/angular.js/2.0.0-beta.17/angular2-all-testing.umd.dev.js')
print(page_)	
document_ = page_.read().decode('utf-8')
# print(document_)

_page_ = urllib.request.urlopen('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
print(_page_)	
_document_ = _page_.read().decode('utf-8')
# print(_document_)

_page = urllib.request.urlopen('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
print(_page)	
_document = _page.read().decode('utf-8')
# print(_document)
# '''


'''异步的得到
class get_lib(threading.Thread):
	def __init__(self,url):
		super().__init__()
		self.url = url
	def run(self):
		page = urllib.request.urlopen(self.url)
		print(page)	
		document = page.read().decode('utf-8')

a = get_lib('https://cdn.bootcss.com/vue/2.4.2/vue.js')
a.start()
b = get_lib('https://cdn.bootcss.com/angular.js/2.0.0-beta.17/angular2-all-testing.umd.dev.js')
b.start()
c = get_lib('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
c.start()
d = get_lib('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
d.start()
a.join()
b.join()
c.join()
d.join()
'''

end = time.time()
print('同步耗费时间{}'.format(end-start))
print('all finish 得到异步执行的时间要小于同步执行的时间,执行十次,对于这个请求,平均每次少0.5s')


