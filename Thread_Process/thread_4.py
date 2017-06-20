import threading
import time 

#setDaemon
print('setDaemon把所有今晨变成主线程的守护进程,主线程结束了,其他也结束了')

class thread_sample(threading.Thread):
	def __init__(self,n):
		self.n = n
		super().__init__()
	def run(self):
		print('this thread name is {}'.format(self.n))
		time.sleep(1)
		print('will wait 2s')
		time.sleep(2)
		print('come to the end')
		time.sleep(1)
		print('fuck')

t1 = thread_sample('first')
t1.setDaemon(True)
t1.start()
t2 = thread_sample('second')
t2.setDaemon(True)
t2.start()


time.sleep(3)
print('This is main process and last 3s')
