import threading
import time

print('this is basic sample')

#普通创建法
'''
def run(n):
	print('task',n)
	time.sleep(1)
	print('2s')
	time.sleep(1)
	print('1s')
	time.sleep(1)
	print('0s')
	time.sleep(1)


t_1 = threading.Thread(target=run,args=('first',))
t_2 = threading.Thread(target=run,args=('second',))

t_1.start()
t_2.start()
'''

#class创建法

class thread_class(threading.Thread):
	def __init__(self,n):
		super().__init__()
		self.n = n
	def run(self):
		print('task',self.n)
		time.sleep(1)
		print('2s')
		time.sleep(1)
		print('1s')
		time.sleep(1)
		print('0s')
		time.sleep(1)
if __name__ == "__main__":
	t_1 = thread_class('first')	
	t_2 = thread_class('second')

	t_1.start()
	t_2.start()

print('this is main thread')

#这样也是先延长时间,在全部显示
# print('fuck')
# time.sleep(1)
# print('fuck')
# time.sleep(1)
# print('fuck')
# time.sleep(1)