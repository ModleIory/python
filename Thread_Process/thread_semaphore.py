import threading
import time

'''
但是如何检验生效呢
'''

class semaphore(threading.Thread):
	def __init__(self,n):
		super().__init__()
		self.sema = threading.BoundedSemaphore(3)
		self.n = n
	def run(self):
		self.sema.acquire()
		time.sleep(1)
		print('this is in semaphore..{}'.format(self.n))
		self.sema.release()

for x in range(10):
	t = semaphore(10)
	t.start()

while threading.active_count() != 1:
	pass
	print(threading.active_count())
else:
	print('allow')