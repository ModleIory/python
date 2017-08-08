import multiprocessing
import os , sys , time
import urllib.request

class get_data(multiprocessing.Process):
	def __init__(self,link):
		super().__init__()
		print('Process is beginning')
		self.url = link
	def run(self):
		page = urllib.request.urlopen(self.url)
		print(page)	
		document = page.read().decode('utf-8')


if __name__ == '__main__':
	start= time.time()
	a = get_data('https://cdn.bootcss.com/vue/2.4.2/vue.js')
	a.start()
	b = get_data('https://cdn.bootcss.com/angular.js/2.0.0-beta.17/angular2-all-testing.umd.dev.js')
	b.start()
	c = get_data('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
	c.start()
	d = get_data('https://cdn.bootcss.com/react/15.6.1/react-dom-server.js')
	d.start()
	a.join()
	b.join()
	c.join()
	d.join()
	end = time.time()
	print('waster time {}'.format(end-start))
	print('The ending')

