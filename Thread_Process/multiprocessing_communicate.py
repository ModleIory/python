
import multiprocessing
import os , time , sys 

q = multiprocessing.Queue()
count = 0

class A(multiprocessing.Process):
	def __init__(self,q):
		super().__init__()
		self.q = q
		print('task A is running ......')
	def run(self):
		for i in range(10):
			print('队列中将要进入{}'.format(i))
			self.q.put(i,block=True)
			time.sleep(4)


class B(multiprocessing.Process):
	def __init__(self,q):
		super().__init__()
		self.q = q
		print('task B is running ......')
	def run(self):
		while  True:
			time.sleep(1)
			print('我得到了队列元素{}'.format(self.q.get(block=True)))
			global count 
			count += 1
			if count>=10:
				sys.exit()

if __name__ == '__main__':
	a = A(q)
	b = B(q)
	a.start()
	time.sleep(2)
	b.start()
	a.join()
	b.join()

	print('All is finished!')