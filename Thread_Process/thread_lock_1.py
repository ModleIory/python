import threading 
import time

num = 10

'''
但是如何检验生效呢
'''

class one(threading.Thread):
	lock = None
	def __init__(self,x):
		super().__init__()
		self.lock = threading.Lock()
		self.x = x
	def run(self):
		global num
		self.lock.acquire()
		num += 2
		self.lock.release()
		print('one print num is {} and id is {}'.format(num,self.x))

class two(threading.Thread):
	lock = None
	def __init__(self,x):
		super().__init__()
		self.lock = threading.Lock()
		self.x = x
	def run(self):
		global num
		self.lock.acquire()
		num -= 1
		self.lock.release()
		print('two print num is {} and id is {}'.format(num,x))



for x in range(500):
	#1如此并发运行,则数据每次结果不一样,是脏数据
	t_1 = one(x)
	t_2 = two(x)
	t_1.start()
	t_2.start()
	#2加了join之后按照顺序就对了
	t_1.join()
	t_2.join()
	#3我来上锁

	
